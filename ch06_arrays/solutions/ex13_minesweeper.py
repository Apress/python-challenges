# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import random

from ch06_arrays.intro.intro import print_array, get_dimension
from ch06_arrays.intro.intro_directions_example import Direction


def place_bombs_randomly(width, height, probability):
    bombs = [[False for x in range(width + 2)] for y in range(height + 2)]

    for y in range(1, len(bombs) - 1):
        for x in range(1, len(bombs[0]) - 1):
            bombs[y][x] = random.random() < probability

    return bombs


def calc_bomb_count(bombs):
    max_y, max_x = get_dimension(bombs)
    bomb_count = [[0 for x in range(max_x)] for y in range(max_y)]

    for y in range(1, max_y - 1):
        for x in range(1, max_x - 1):
            if not bombs[y][x]:
                for current_dir in Direction:
                    dx, dy = current_dir.to_dx_dy()
                    if bombs[y + dy][x + dx]:
                        bomb_count[y][x] += 1
            else:
                bomb_count[y][x] = 9

    return bomb_count


def print_board(bombs, bomb_symbol, solution):
    for y in range(1, len(bombs) - 1):
        for x in range(1, len(bombs[0]) - 1):
            if bombs[y][x]:
                print(bomb_symbol, end=" ")
            elif solution is not None and len(solution) != 0:
                print(solution[y][x], end=" ")
            else:
                print(".", end=" ")

        print()
    print()


def main():
    bombs = place_bombs_randomly(10, 5, 0.5)
    print_board(bombs, "B", None)

    bomb_counts = calc_bomb_count(bombs)
    print_board(bombs, "B", bomb_counts)


if __name__ == "__main__":
    main()
