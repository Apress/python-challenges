# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import numpy as np
import sys


numbers = [i for i in range(100_000)]

print("Size of each element: ", sys.getsizeof(numbers[0]))
print(numbers[99_999])
print("Size of the list: ", sys.getsizeof(numbers))

numbers_array = np.arange(100_000)

print("Size of each element: ", numbers_array.itemsize)
print(numbers_array[99_999])
print("Size of the Numpy array: ", sys.getsizeof(numbers_array))
