# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import numpy as np

from ch06_arrays.solutions.ex08_add_one import add_one


def main():
    # Wrap result in numpy array
    result = add_one(np.array([1, 3, 2, 4]))
    result_as_array = np.array(result)
    print(result)  # [1, 3, 2, 5]
    print(result_as_array)  # [1 3 2 5]

    print(add_one(np.array([1, 4, 8, 9])))  # [1, 4, 9, 0]
    print(add_one(np.array([9, 9, 9, 9])))  # [1, 0, 0, 0, 0]


if __name__ == "__main__":
    main()
