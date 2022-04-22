# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import numpy as np

from ch06_arrays.intro.intro_numpy_array_creation import get_dimension


def main():
    world = np.array([list("################"),
                      list("##  P         ##"),
                      list("####   $ X  ####"),
                      list("###### $  ######"),
                      list("################")])
    print(world)
    print_array(world)


def print_array(values):
    max_y, max_x = get_dimension(values)
    for y in range(max_y):
        for x in range(max_x):
            value = values[y][x]
            print(value, end=" ")

        print()


if __name__ == "__main__":
    main()
