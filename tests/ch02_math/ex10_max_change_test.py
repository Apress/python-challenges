# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

## PYTEST
from ch02_math.solutions.ex10_max_change import calc_max_possible_change


@pytest.mark.parametrize("coins, max_change",
                         [([1], 1),
                          ([1, 1], 2),
                          ([1, 5], 1),
                          ([1, 2, 4], 7),
                          ([1, 2, 3, 7], 13),
                          ([1, 2, 3, 8], 6),
                          ([1, 1, 1, 1, 5, 10, 20, 50], 39)])
def test_calc_max_possible_change(coins, max_change):
    assert calc_max_possible_change(coins) == max_change
