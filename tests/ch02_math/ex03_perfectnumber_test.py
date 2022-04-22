# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import pytest

from ch02_math.solutions.ex03_perfectnumber import is_perfect_number_simple, calc_perfect_numbers, is_perfect_number_based_on_proper_divisors


@pytest.mark.parametrize("n, expected",
                         [(6, True), (28, True),
                          (496, True), (8128, True)])
def test_is_perfect_number_simple(n, expected):
    assert is_perfect_number_simple(n) == expected


@pytest.mark.parametrize("n, expected", [(50, [6, 28]),
                                         (1000, [6, 28, 496]),
                                         (10000, [6, 28, 496, 8128])])
def test_calc_perfect_numbers(n, expected):
    assert calc_perfect_numbers(n) == expected


@pytest.mark.parametrize("n, expected", [
    (6, True), (28, True), (496, True), (8128, True)])
def test_is_perfect_number_based_on_proper_divisors(n, expected):
    assert is_perfect_number_based_on_proper_divisors(n) == expected
