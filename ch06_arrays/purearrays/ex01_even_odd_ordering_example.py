# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import array

import numpy as np

from ch06_arrays.solutions.ex01_even_odd_ordering import order_even_before_odd, order_even_before_odd_optimized


def main():

    # Python array
    print("working on pure arrays")
    values = array.array('i', [1, 2, 3, 4, 5, 6, 7])
    print(order_even_before_odd(values))
    print(values)

    values = array.array('i', [1, 2, 3, 4, 5, 6, 7])
    print(order_even_before_odd(values))

    values = array.array('i', [2, 4, 6, 1, 8])
    print(order_even_before_odd(values))

    values = array.array('i', [2, 4, 6, 8, 1])
    print(order_even_before_odd(values))

    values = array.array('i', [])
    print(order_even_before_odd(values))

    print("#######################################")

    # Numpy array
    print("working on Num PY pure arrays")
    values = np.array([1, 2, 3, 4, 5, 6, 7])
    print(order_even_before_odd(values))
    print(values)

    values = np.array([1, 2, 3, 4, 5, 6, 7])
    print(order_even_before_odd(values))

    values = np.array([2, 4, 6, 1, 8])
    print(order_even_before_odd(values))

    values = np.array([2, 4, 6, 8, 1])
    print(order_even_before_odd(values))

    values = np.array([])
    print(order_even_before_odd(values))

    print(order_even_before_odd_optimized(np.array([1, 2, 3, 4, 5, 6, 7])))
    print(order_even_before_odd_optimized(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])))

    print(order_even_before_odd_optimized(np.array([2, 4, 6, 1, 8])))
    print(order_even_before_odd_optimized(np.array([2, 4, 6, 8, 1])))
    print(order_even_before_odd_optimized(np.array([])))


if __name__ == "__main__":
    main()
