# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import functools


def sum(n):
    return functools.reduce(lambda n_1, n: n_1 + n, range(1, n + 1))


def factorial(n):
    return functools.reduce(lambda n_1, n: n_1 * n, range(1, n + 1))


print(functools.reduce(lambda fir, sec: fir + sec, range(1, 10)))
for i in range(1, 10):
    print("i:", i)
    print("sum:", sum(i))
    print("fac", factorial(i))
