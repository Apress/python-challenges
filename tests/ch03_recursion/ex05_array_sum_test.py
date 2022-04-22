# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch03_recursion.solutions.ex05_array_sum import sum_rec, sum_tail, sum_lambda


@pytest.mark.parametrize("values, expected",
                         [([1], 1), ( [1, 2, 3], 6), ([1, 2, 3, -7], -1)])
def test_sum_rec(values, expected):
    assert sum_rec(values) == expected


@pytest.mark.parametrize("values, expected",
                         [([1], 1), ( [1, 2, 3], 6), ([1, 2, 3, -7], -1)])
def test_sum_tail(values, expected):
    assert sum_tail(values) == expected


@pytest.mark.parametrize("values, expected",
                         [([1], 1), ( [1, 2, 3], 6), ([1, 2, 3, -7], -1)])
def test_sum_lambdal(values, expected):
    assert sum_lambda(values) == expected
