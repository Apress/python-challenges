# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch03_recursion.solutions.ex08_power_of import is_power_of_2, power_of_iterative, power_of, power_of_optimized


@pytest.mark.parametrize("value, expected",
                         [(2, True), (3, False), (4, True),
                          (10, False), (16, True)])
def test_is_power_of2(value, expected):
    assert is_power_of_2(value) == expected


def inputs_and_expected():
    return [(2, 2, 4), (4, 2, 16), (16, 2, 256),
            (4, 4, 256), (2, 8, 256), (3, 3, 27)]


@pytest.mark.parametrize("number, exponent, expected",
                         inputs_and_expected())
def test_power_of(number, exponent, expected):
    assert power_of(number, exponent) == expected


@pytest.mark.parametrize("number, exponent, expected",
                         inputs_and_expected())
def test_power_of_optimized(number, exponent, expected):
    assert power_of_optimized(number, exponent) == expected


@pytest.mark.parametrize("number, exponent, expected",
                         inputs_and_expected())
def test_power_of_iterative(number, exponent, expected):
    assert power_of_iterative(number, exponent) == expected
