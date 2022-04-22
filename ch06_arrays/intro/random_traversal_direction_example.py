# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import numpy as np

from ch06_arrays.intro.intro_directions_example import Direction


def main():
    world = np.array([list("ABCDEF"),
                      list("GHIJKL"),
                      list("MNOPQR"),
                      list("abcdef"),
                      list("ghijkl")])

    dir = Direction.provide_random_direction()
    print("Direction:", dir.name)

    pos_x = 0
    pos_y = 0
    steps = 0

    while steps < 25:
        print(world[pos_y][pos_x], " ", end="")

        dx, dy = dir.to_dx_dy()
        if not is_on_board(world, pos_x + dx, pos_y + dy):
            dir = select_new_dir(world, dir, pos_x, pos_y)
            dx, dy = dir.to_dx_dy()
            print("\nNew Direction:", dir.name)

        pos_x += dx
        pos_y += dy
        steps += 1


def select_new_dir(world, dir, pos_x, pos_y):
    old_dir = dir
    while True:
        dir = Direction.provide_random_direction()
        dx, dy = dir.to_dx_dy()
        if old_dir != dir and is_on_board(world, pos_x + dx, pos_y + dy):
            break

    return dir


def is_on_board(values, next_pos_x, next_pos_y):
    max_y, max_x = values.shape

    return 0 <= next_pos_x < max_x and 0 <= next_pos_y < max_y


if __name__ == "__main__":
    main()
