# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import random

from ch06_arrays.intro.intro import print_array, get_dimension


# Terminiert ggf. nicht!!
def init_jewels_board_v1(width, height, num_of_colors):
    board = []
    for y in range(height):
        board.append([])
        for x in range(width):
            board[y].append(0)

    for y in range(height):
        for x in range(width):
            board[y][x] = select_valid_jewel(board, x, y, num_of_colors)

    return board


def init_jewels_board(width, height, num_of_colors):
    board = [[0 for x in range(width)] for y in range(height)]

    for y in range(height):
        for x in range(width):
            board[y][x] = select_valid_jewel(board, x, y, num_of_colors)

    return board


def select_valid_jewel(board, x, y, num_of_colors):
    next_jewel_nr = -1
    is_valid = False

    while not is_valid:
        next_jewel_nr = random.randint(1, num_of_colors)

        is_valid = not check_horizontally(board, x, y, next_jewel_nr) and \
                   not check_vertically(board, x, y, next_jewel_nr) and \
                   not check_diagonally(board, x, y, next_jewel_nr)

    return next_jewel_nr


def check_horizontally(board, x, y, jewel_nr):
    top1 = get_at(board, x, y - 1)
    top2 = get_at(board, x, y - 2)

    return top1 == jewel_nr and top2 == jewel_nr


def check_vertically(board, x, y, jewel_nr):
    left1 = get_at(board, x - 1, y)
    left2 = get_at(board, x - 2, y)

    return left1 == jewel_nr and left2 == jewel_nr


def get_at(values, x, y):
    max_y, max_x = get_dimension(values)
    if x < 0 or y < 0 or y >= max_y or x >= max_x:
        return -1

    return values[y][x]


# Bonus
def check_diagonally(board, x, y, jewel_nr):
    up_left1 = get_at(board, x - 1, y - 1)
    up_left2 = get_at(board, x - 2, y - 2)

    up_right1 = get_at(board, x + 1, y - 1)
    up_right2 = get_at(board, x + 2, y - 2)

    return up_left1 == jewel_nr and up_left2 == jewel_nr or \
           up_right1 == jewel_nr and up_right2 == jewel_nr


def check_board_validity(board2dim):
    errors = []

    max_y, max_x = get_dimension(board2dim)
    for y in range(max_y):
        for x in range(max_x):

            current_jewel = board2dim[y][x]

            has_chain_hor = check_horizontally(board2dim, x, y, current_jewel)
            has_chain_ver = check_vertically(board2dim, x, y, current_jewel)
            has_chain_dia = check_diagonally(board2dim, x, y, current_jewel)

            if has_chain_hor or has_chain_ver or has_chain_dia:
                error_msg = "Invalid at x={} y={} hor={}, ver={}, dia={}". \
                    format(x, y, has_chain_hor, has_chain_ver, has_chain_dia)
                errors.append(error_msg)

    return errors


def main():
    # Terminiert ggf. nicht!! wenn nur 1-3 möglich sind
    print("Init 10 x 5 * 4")
    print_array(init_jewels_board(10, 5, 4))

    print("Init 15 x 7 * 5")
    print_array(init_jewels_board(15, 7, 5))

    ###############################

    values_with_errors = [[2, 3, 3, 4, 4, 3, 2],
                          [1, 3, 3, 1, 3, 4, 4],
                          [4, 1, 4, 3, 3, 1, 3],
                          [2, 2, 1, 1, 2, 3, 2],
                          [3, 2, 4, 4, 3, 3, 4]]

    print_array(values_with_errors)
    print(check_board_validity(values_with_errors))

    values2 = [[2, 3, 3, 4, 4, 3, 2],
               [1, 3, 3, 1, 3, 4, 4],
               [4, 1, 4, 5, 3, 1, 3],
               [2, 2, 5, 1, 2, 3, 2],
               [3, 2, 4, 4, 5, 3, 4]]

    print_array(values2)
    print(check_board_validity(values2))


if __name__ == "__main__":
    main()
