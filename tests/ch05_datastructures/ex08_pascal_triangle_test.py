# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch05_datastructures.solutions.ex08_pascal_triangle import pascal


@pytest.mark.parametrize("n, expected",
                         [(1, [[1]]),
                          (2, [[1], [1, 1]]),
                          (3, [[1], [1, 1], [1, 2, 1]]),
                          (4, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])])
def test_pascal(n, expected):
    result = pascal(n)

    assert expected == result
