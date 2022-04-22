# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch03_recursion.solutions.ex03_gcd import gcd, gcd_iterative, lcm


@pytest.mark.parametrize("a, b, expected",
                         [(42, 7, 7), (42, 28, 14), (42, 14, 14)])
def test_gcd(a, b, expected):
    assert gcd(a, b) == expected


@pytest.mark.parametrize("a, b, expected",
                         [(42, 7, 7), (42, 28, 14), (42, 14, 14)])
def test_gcd_iterative(a, b, expected):
    assert gcd_iterative(a, b) == expected


@pytest.mark.parametrize("a, b, expected",
                         [(2, 7, 14), (7, 14, 14), (42, 14, 42),
                          (54, 24, 216)])
def test_lcm(a, b, expected):
    assert lcm(a, b) == expected
