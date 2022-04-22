# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import numpy as np

from ch06_arrays.intro.intro import print_array, get_dimension, swap


def flip_horizontally(values2dim):
    max_y, max_x = get_dimension(values2dim)

    for y in range(max_y):
        left_idx = 0
        right_idx = max_x - 1

        while left_idx < right_idx:
            left_value = values2dim[y][left_idx]
            right_value = values2dim[y][right_idx]

            # swap
            values2dim[y][left_idx] = right_value
            values2dim[y][right_idx] = left_value

            left_idx += 1
            right_idx -= 1


def flip_vertically(values2dim):
    max_y, max_x = get_dimension(values2dim)
    for x in range(max_x):
        top_idx = 0
        bottom_idx = max_y - 1

        while top_idx < bottom_idx:
            top_value = values2dim[top_idx][x]
            bottom_value = values2dim[bottom_idx][x]

            # swap
            values2dim[top_idx][x] = bottom_value
            values2dim[bottom_idx][x] = top_value

            top_idx += 1
            bottom_idx -= 1


def flip_horizontally_v2(values2dim):
    max_y, max_x = get_dimension(values2dim)
    for y in range(max_y):
        row = values2dim[y]
        for x in range(max_x // 2):
            swap(row, x, max_x - x - 1)


def flip_vertically_just_for_lists(values2dim):
    max_y, _ = get_dimension(values2dim)
    for y in range(max_y // 2):
        swap(values2dim, y, max_y - y - 1)


def main():
    hori_values = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]

    flip_horizontally(hori_values)

    print(hori_values)
    print_array(hori_values)

    vert_values = [[1, 1, 4, 4],
                   [2, 2, 5, 5],
                   [3, 3, 6, 6]]

    flip_vertically(vert_values)
    print_array(vert_values)

    hori_values = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]

    flip_horizontally_v2(hori_values)

    print(hori_values)
    print_array(hori_values)

    vert_values = [[1, 1, 4, 4],
                   [2, 2, 5, 5],
                   [3, 3, 6, 6]]

    flip_vertically_just_for_lists(vert_values)
    print_array(vert_values)


if __name__ == "__main__":
    main()
