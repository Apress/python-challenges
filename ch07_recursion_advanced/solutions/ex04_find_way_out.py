# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def get_at(values, x, y):
    return values[y][x]


def print_array(values):
    for y in range(0, len(values)):
        for x in range(0, len(values[y])):
            value = get_at(values, x, y)
            print(value, end='')
        print()

def find_way_out(values, x, y):
    if x < 0 or y < 0 or x > len(values[0]) or y >= len(values):
        return False

    # rekursiver Abbruch
    if get_at(values, x, y) == 'X':
        print("FOUND EXIT: x: {}, y: {}".format(x, y))
        return True

    # Mauer oder bereits besucht?
    if get_at(values, x, y) in '#.':
        return False

    # rekursiver Abstieg
    if get_at(values, x, y) == ' ':
        #   markiere als besucht
        values[y][x] = '.'

        # versuche alle 4 Himmelsrichtungen
        up = find_way_out(values, x, y - 1)
        left = find_way_out(values, x + 1, y)
        down = find_way_out(values, x, y + 1)
        right = find_way_out(values, x - 1, y)

        found_a_way = up or left or down or right

        # Backtracking, weil keine gültige Lösung
        if not found_a_way:
            # falscher Weg, somit Feldmarkierung löschen
            values[y][x] = ' '

        return found_a_way

    raise ValueError("wrong char in labyrinth")


def find_way_out_v2(board, x, y):
    if board[y][x] == '#':
        return False

    found = board[y][x] == 'X'
    if found:
        print("FOUND EXIT: x: {}, y: {}".format(x, y))

    board[y][x] = '#'

    right = find_way_out_v2(board, x + 1, y)
    left = find_way_out_v2(board, x - 1, y)
    down = find_way_out_v2(board, x, y + 1)
    up = find_way_out_v2(board, x, y - 1)

    return found or right or left or down or up


def main():
    world_big = [list("##################################"),
                 list("# #         #    #     #  #   X#X#"),
                 list("#  ##### #### ##   ##  #  # ###  #"),
                 list("#  ##  #    #  ## ##  #  #     # #"),
                 list("#    #  ###  # ## ##   #   ### # #"),
                 list("# #   ####     ## ##      ###  # #"),
                 list("####   #     ####  ####  # ####  #"),
                 list("######   #########   ##   # ###  #"),
                 list("##     #  X X####X #  #  # ###  ##"),
                 list("##################################")]

    print_array(world_big)
    if find_way_out(world_big, 1, 1):
        print_array(world_big)

    world_big = [list("##################################"),
                 list("# #         #    #     #  #   X#X#"),
                 list("#  ##### #### ##   ##  #  # ###  #"),
                 list("#  ##  #    #  ## ##  #  #     # #"),
                 list("#    #  ###  # ## ##   #   ### # #"),
                 list("# #   ####     ## ##      ###  # #"),
                 list("####   #     ####  ####  # ####  #"),
                 list("######   #########   ##   # ###  #"),
                 list("##     #  X X####X #  #  # ###  ##"),
                 list("##################################")]

    print_array(world_big)
    if find_way_out_v2(world_big, 1, 1):
        print_array(world_big)


if __name__ == "__main__":
    main()
