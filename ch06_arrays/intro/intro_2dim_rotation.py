# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from enum import Enum, auto

import numpy as np


class RotationDirection(Enum):
    LEFT_90 = auto()
    RIGHT_90 = auto()


def rotate(values, dir):
    orig_length_y, orig_length_x = values.shape

    rotated_array = np.empty((orig_length_x, orig_length_y), values.dtype)

    for y in range(orig_length_y):
        for x in range(orig_length_x):
            max_x = orig_length_x - 1
            max_y = orig_length_y - 1

            orig_value = values[y][x]

            if dir == RotationDirection.LEFT_90:
                new_x = y
                new_y = max_x - x
                rotated_array[new_y][new_x] = orig_value

            if dir == RotationDirection.RIGHT_90:
                new_x = max_y - y
                new_y = x
                rotated_array[new_y][new_x] = orig_value

    return rotated_array


def main():
    letters = np.array([["A", "B", "C", "D"],
                        ["E", "F", "G", "H"]])

    left_rotated = rotate(letters, RotationDirection.LEFT_90)
    print(left_rotated)
    right_rotated = rotate(letters, RotationDirection.RIGHT_90)
    print(right_rotated)


if __name__ == "__main__":
    main()
