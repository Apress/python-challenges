# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

## PYTEST
from ch02_math.solutions.ex05_prime_pairs_optimized2 import calc_pairs


@pytest.mark.parametrize("n, expected",
                         [(2, {3: 5, 5: 7, 11: 13, 17: 19, 29: 31, 41: 43}),
                          (4, {3: 7, 7: 11, 13: 17, 19: 23, 37: 41, 43: 47}),
                          (6, {5: 11, 7: 13, 11: 17, 13: 19, 17: 23, 23: 29,
                               31: 37, 37: 43, 41: 47, 47: 53})])
def test_calc_pairs(n, expected):
    max_value = 50

    assert calc_pairs(max_value, n) == expected
