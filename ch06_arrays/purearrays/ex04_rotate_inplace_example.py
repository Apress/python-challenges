# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import numpy as np

from ch06_arrays.solutions.ex04_rotate_inplace import rotate_inplace_recursive, rotate_inplace
from ch06_arrays.intro.intro import print_array


def main():
    values = [
        ['1', '2', '3', '4', '5', '6'],
        ['J', 'K', 'L', 'M', 'N', '7'],
        ['I', 'V', 'W', 'X', 'O', '8'],
        ['H', 'U', 'Z', 'Y', 'P', '9'],
        ['G', 'T', 'S', 'R', 'Q', '0'],
        ['F', 'E', 'D', 'C', 'B', 'A']
    ]

    arr = np.array(values)
    print_array(arr)
    print("------- ROTATED --------")
    rotate_inplace(arr)
    print_array(arr)

    print("==============================")

    values = [
        ['1', '2', '3', '4', '5', '6'],
        ['J', 'K', 'L', 'M', 'N', '7'],
        ['I', 'V', 'W', 'X', 'O', '8'],
        ['H', 'U', 'Z', 'Y', 'P', '9'],
        ['G', 'T', 'S', 'R', 'Q', '0'],
        ['F', 'E', 'D', 'C', 'B', 'A']

    ]

    arr = np.array(values)
    print_array(arr)
    print("------- ROTATED --------")
    rotate_inplace_recursive(arr)
    print_array(arr)


if __name__ == "__main__":
    main()
