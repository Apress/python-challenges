# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import sys
import time

import numpy as np

numbers = [1, 2, 3, 4, 5, 6, 7]
numbers_array = np.array(numbers)
firstprimes = [2, 3, 5, 7, 11, 13, 17]
primes = np.array(firstprimes)

print(numbers)
print(primes)


array_with_zeros = np.zeros((2, 4), dtype='int')
print(array_with_zeros)

array_with_ones = np.ones((5, 10))
print(array_with_ones)

empty_strings_array = np.empty((3, 3), dtype="str")
print(empty_strings_array)


zeros_with_lists = [[0 for x in range(4)] for y in range(2)]
print(zeros_with_lists)

ones_with_lists = [[1 for x in range(10)] for y in range(5)]
print(ones_with_lists)

empty_strign_with_list = [["" for x in range(3)] for y in range(3)]
print(empty_strign_with_list)

empty_strign_with_list[1][1] = "M"
print(empty_strign_with_list)

width = 8
height = 8
board = [[0] * width] * height
print(board)

# Achtung: Modifikation geschieht in allen Zeilen!
board[1][1] = 1
print(board)


twodim = np.array([["A1", "A2"],
                   ["B1", "B2"],
                   ["C1", "C2"]])
print(twodim)

print(len(twodim)) # 3
print(twodim.size) # 6
print(twodim.shape) # (3, 2)


# size
numbers = [i for i in range(10_000)]
numbers_array = np.array(numbers)
numbers_as_array = np.asarray(numbers)
numbers_ones_array = np.ones(10_000)

print("Memory consumption")
print("list:", sys.getsizeof(numbers)) # 87616
print("array:", sys.getsizeof(numbers_array)) # 80096
print("array:", sys.getsizeof(numbers_as_array)) # 8 * 10_000 + 96
print("array:", sys.getsizeof(numbers_ones_array)) # 8 * 10_000 + 96



# performance
numbers = [i for i in range(1_000_000)]
numbers_array = np.array(numbers)

start = time.process_time()
for i in range(len(numbers)):
    numbers[i] *= 7
end = time.process_time()
print(numbers[:10])
print("list access took %.2f ms" % ((end - start) * 1000))

start = time.process_time()
for i in range(len(numbers)):
    numbers_array[i] *= 7
end = time.process_time()
print(numbers_array[:10])
print("array access took %.2f ms" % ((end - start) * 1000))




