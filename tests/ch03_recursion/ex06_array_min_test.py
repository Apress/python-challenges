# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import sys

import pytest

from ch03_recursion.solutions.ex06_array_min import min_rec


@pytest.mark.parametrize("values, expected",
                         [([7, 2, 1, 9, 7, 1 ], 1), ([1, 2, 3, -7], -7),
                          ([11, 2, 33, 44, 55, 6, 7], 2), ([], sys.maxsize)])
def test_min_rec(values, expected):
    assert min_rec(values) == expected
