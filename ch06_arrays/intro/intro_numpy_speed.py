# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


# importing required packages
import random

import numpy as np
import time

# Indexzugriffe sind mit Listen schneller für bis ca. 1000 Elemente
for size in (100, 1000, 10000, 100000, 1_000_000):

    print("performing idx assign for ", size, "elements")

    list = range(size)
    array = np.asarray(list)
    result_list = list[:]
    result_array = array[:]

    start = time.process_time()
    for i in range(size):
        result_list = list[size - 1 - i]
    end = time.process_time()
    print("list idx assign took %.2f ms" % ((end - start) * 1000))

    start = time.process_time()
    for i in range(size):
        result_array[i] = array[size - 1 - i]
    end = time.process_time()
    print("array idx assign took %.2f ms" % ((end - start) * 1000))

for size in (100, 1000, 10000, 100000, 1_000_000):
    print("performing '+5' for all", size, "elements")

    list1 = range(size)
    array1 = np.asarray(list1)

    start = time.process_time()
    result_list = [i + 5 for i in range(size)]
    end = time.process_time()
    print("list '+5' took %.2f ms" % ((end - start) * 1000))

    start = time.process_time()
    result_array = array1 + 5
    end = time.process_time()
    print("array '+5' took %.2f ms" % ((end - start) * 1000))


############################# DOT PRODUCT #####################

def python_implementation(arr1, arr2):
    result = [[0 for _ in range(len(arr1))] for _ in range(len(arr2[0]))]

    for row in range(len(arr1)):
        for x1_y2 in range(len(arr2[0])):
            for y2 in range(len(arr2)):
                result[row][x1_y2] += arr1[row][y2] * arr2[y2][x1_y2]
    return result


def numpy_implementation(arr1, arr2):
    return np.array(arr1).dot(arr2)


def generate(size, range_):
    arr = [[[random.randrange(*range_) for _ in range(size)] for _ in range(size)] for _ in range(2)]
    return arr


max_x = 100
max_y = 50
arr1 = [[random.randrange(1, 100) for _ in range(max_x)] for _ in range(max_y)]
arr2 = [[random.randrange(1, 100) for _ in range(max_y)] for _ in range(max_x)]

start = time.process_time()
python_implementation(arr1, arr2)
end = time.process_time()
print("list perform dot product took %.2f ms" % ((end - start) * 1000))

start = time.process_time()
numpy_implementation(arr1, arr2)
end = time.process_time()
print("array perform dot product took %.2f ms" % ((end - start) * 1000))

# Aufgabe PYTHON: Matrixmultiplikation
arr1 = [[1, 2, 3],
        [4, 5, 6]]

arr2 = [[10, 1],
        [5, 5],
        [1, 10]]

result1 = python_implementation(arr1, arr2)
print(result1)
# [[12, 21], [45, 54]]

result2 = numpy_implementation(arr1, arr2)
print(result2)

