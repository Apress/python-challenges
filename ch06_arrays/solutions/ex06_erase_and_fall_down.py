# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch06_arrays.intro.intro import print_array, get_dimension
from ch06_arrays.intro.intro_directions_example import Direction


def erase_chains(values2dim):
    mark_elements_for_removal(values2dim)

    return erase_all_marked(values2dim)


def mark_elements_for_removal(values2dim):
    max_y, max_x = get_dimension(values2dim)

    for y in range(max_y):
        for x in range(max_x):
            dirs_with_chains = find_chains(values2dim, x, y)

            mark_chains_for_removal(values2dim, x, y, dirs_with_chains)


def erase_all_marked(values2dim):
    max_y, max_x = get_dimension(values2dim)

    erased_something = False

    for y in range(max_y):
        for x in range(max_x):
            if is_element_marked_for_removal(values2dim[y][x]):
                values2dim[y][x] = 0
                erased_something = True

    return erased_something


def is_element_marked_for_removal(value):
    return value < 0


def find_chains(values2dim, start_x, start_y):
    orig_value = values2dim[start_y][start_x]
    if orig_value == 0:  # ACHTUNG an solche Spezialfälle denken
        return []

    dirs_with_chains = []

    relevant_dirs = (Direction.S, Direction.SW, Direction.E, Direction.SE)

    for current_dir in relevant_dirs:
        length = 1

        dx, dy = current_dir.value
        next_pos_x = start_x + dx
        next_pos_y = start_y + dy

        while is_on_board(values2dim, next_pos_x, next_pos_y) and \
            is_same(orig_value, values2dim[next_pos_y][next_pos_x]):
            length += 1
            next_pos_x += dx
            next_pos_y += dy

            if length >= 3:
                dirs_with_chains.append(current_dir)

    return dirs_with_chains


def is_on_board(values2dim, next_pos_x, next_pos_y):
    max_y, max_x = get_dimension(values2dim)
    return next_pos_x >= 0 and next_pos_y >= 0 and \
           next_pos_x < max_x and next_pos_y < max_y


def is_same(val1, val2):
    return abs(val1) == abs(val2)


def mark_chains_for_removal(values, start_x, start_y, dirs_with_chains):
    orig_value = values[start_y][start_x]

    for current_dir in dirs_with_chains:
        dx, dy = current_dir.value
        next_x = start_x
        next_y = start_y

        while (is_on_board(values, next_x, next_y) and \
               is_same(orig_value, values[next_y][next_x])):
            values[next_y][next_x] = mark_element_for_removal(orig_value)

            next_x += dx
            next_y += dy


def mark_element_for_removal(value):
    return -value if value > 0 else value


def fall_down_first_try(values2dim):
    max_y, max_x = get_dimension(values2dim)

    for x in range(max_x):
        for y in range(max_y - 1, 0, -1):
            value = values2dim[y][x]
            if is_blank(value):
                # fall down
                values2dim[y][x] = values2dim[y - 1][x]
                values2dim[y - 1][x] = 0


def is_blank(value):
    return value == 0


def fall_down(values2dim):
    max_y, max_x = get_dimension(values2dim)

    for x in range(max_x):
        for y in range(max_y - 1, 0, -1):
            current_y = y
            # so lange runterfallen, bis darunter kein Leerraum mehr existiert
            while current_y < len(values2dim) and \
                  is_blank(values2dim[current_y][x]):
                # runterfallen
                values2dim[current_y][x] = values2dim[current_y - 1][x]
                values2dim[current_y - 1][x] = 0

                current_y += 1


def main():
    example_board = [[1, 1, 1, 2, 4, 4, 3],
                  [1, 1, 3, 4, 2, 4, 3],
                  [1, 3, 1, 1, 2, 2, 3]]

    print_array(example_board)
    while (erase_chains(example_board)):
        print("---------------------------------")
        fall_down(example_board)
        print_array(example_board)

    print("---------------------------------")
    print("---------------------------------")
    book_example = [[1, 2, 3, 3, 3, 4],
                    [1, 3, 2, 4, 2, 4],
                    [1, 2, 4, 2, 4, 4],
                    [1, 2, 3, 5, 5, 5],
                    [1, 2, 1, 3, 4, 4]]


    book_example2 = [[1, 1, 1, 2],
                     [1, 1, 3, 4],
                     [1, 2, 1, 3]]

    if erase_chains(book_example2):
        print("ERASED chains")
        print_array(book_example2)

    print("-------------------")
    print("-------------------")
    fall_down_example = [[0, 1, 3, 3, 0, 0],
                         [0, 1, 0, 0, 0, 0],
                         [0, 0, 3, 3, 0, 0],
                         [0, 0, 0, 3, 3, 4],
                         [0, 0, 3, 0, 0, 0]]
    print_array(fall_down_example)

    # 0 1 3 3 0 0      0 0 0 0 0 0
    # 0 1 0 0 0 0      0 0 0 0 0 0
    # 0 0 3 3 0 0  =>  0 0 3 3 0 0
    # 0 0 0 3 3 4      0 1 3 3 0 0
    # 0 0 3 0 0 0      0 1 3 3 3 4

    print("-------------------")
    fall_down_first_try(fall_down_example)
    print_array(fall_down_example)

    print("-------------------")
    print("-------------------")
    print("-------------------")
    fall_down_example = [[0, 1, 3, 3, 0, 0],
                         [0, 1, 0, 0, 0, 0],
                         [0, 0, 3, 3, 0, 0],
                         [0, 0, 0, 3, 3, 4],
                         [0, 0, 3, 0, 0, 0]]
    print_array(fall_down_example)
    print("-------------------")
    fall_down(fall_down_example)
    print_array(fall_down_example)


if __name__ == "__main__":
    main()
