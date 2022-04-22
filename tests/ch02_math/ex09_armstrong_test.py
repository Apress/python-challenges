# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

from ch02_math.solutions.ex09_armstrong import calc_armstrong_numbers, calc_numbers


def test_calc_armstrong_numbers():
    assert calc_armstrong_numbers() == [153, 371]


def test_calc_numbers():
    armstrong_as_lambda = lambda x, y, z: int(pow(x, 3) + pow(y, 3) + pow(z, 3))

    assert calc_numbers(armstrong_as_lambda) == [153, 371]

