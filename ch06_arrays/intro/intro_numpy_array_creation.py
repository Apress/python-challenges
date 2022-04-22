# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import numpy as np


numbers = [1, 2, 3, 4, 5, 6, 7]
numbers_array = np.array(numbers)

firstprimes = [2, 3, 5, 7, 11, 13, 17]
firstprimes_array = np.array(firstprimes)

print(numbers_array)
print(firstprimes_array)


twodim = np.array([["A1", "A2"],
                   ["B1", "B2"],
                   ["C1", "C2"]])
print(twodim)

print(len(twodim)) # 3
print(twodim.size) # 6
print(twodim.shape) # (3, 2)


def get_dimension(values):
    if isinstance(values, list):
        return len(values), len(values[0])

    if isinstance(values, np.ndarray):
        return values.shape

    raise ValueError("unsupported type", type(values))


nested_lists = [[0, 1, 2, 3],
                [4, 5, 6, 7],
                [8, 9, 10, 10]]
nested_lists_array = np.array(nested_lists)
print(get_dimension(nested_lists))
print(get_dimension(nested_lists_array))

#########################################

array_with_zeros = np.zeros((2, 4), dtype='int')
print(array_with_zeros)

array_with_ones = np.ones((5, 10))
print(array_with_ones)

empty_strings_array = np.empty((3, 3), dtype="str")
print(empty_strings_array)

#########################################
zeros_with_lists = [[0 for x in range(4)] for y in range(2)]
print(zeros_with_lists)

ones_with_lists = [[1 for x in range(10)] for y in range(5)]
print(ones_with_lists)

empty_string_with_list = [["" for x in range(3)] for y in range(3)]
print(empty_string_with_list)
