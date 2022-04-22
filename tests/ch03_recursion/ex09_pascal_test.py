# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch03_recursion.solutions.ex09_pascal_triangle import calc_pascal_with_action


@pytest.mark.parametrize("n, expected",
                         [(1, [1]),
                          (2, [1, 1]),
                          (3, [1, 2, 1]),
                          (4, [1, 3, 3, 1]),
                          (5, [1, 4, 6, 4, 1]),
                          (6, [1, 5, 10, 10, 5, 1]),
                          (7, [1, 6, 15, 20, 15, 6, 1])])
def test_calc_pascal_with_action(n, expected):
    assert calc_pascal_with_action(n, None) == expected
