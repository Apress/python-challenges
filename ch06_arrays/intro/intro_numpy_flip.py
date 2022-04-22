# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import numpy as np

numbers = np.array([[1, 2, 3, 4],
                    [1, 2, 3, 4],
                    [1, 2, 3, 4]])
print(np.flip(numbers, 1))

numbers2 = np.array([[1, 1, 1, 1],
                    [2, 2, 2, 2],
                    [3, 3, 3, 3]])
print(np.flip(numbers2, 0))
