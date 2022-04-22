# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import numpy as np

from ch06_arrays.solutions.ex02_flip import flip_horizontally, flip_vertically, flip_horizontally_v2
from ch06_arrays.intro.intro import print_array


def main():

    print("working on Num PY purearrays")
    hori_values = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]

    arr = np.array(hori_values)
    flip_horizontally(arr)

    print(hori_values)
    print_array(arr)

    vert_values = [[1, 1, 4, 4],
                   [2, 2, 5, 5],
                   [3, 3, 6, 6]]

    arr = np.array(vert_values)
    print(len(arr))
    print(arr.shape)

    flip_vertically(arr)
    print_array(arr)

    print("----------")
    print("----------")
    tmp = arr[2]
    arr[2] = arr[0]
    arr[0] = tmp
    print_array(arr)

    # -----------------------------

    hori_values = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]

    arr = np.array(hori_values)
    flip_horizontally_v2(arr)

    print(hori_values)
    print_array(arr)


if __name__ == "__main__":
    main()
