# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch05_datastructures.solutions.ex09_magic_triangle import is_magic_triangle, is_magic_triangle_v2


@pytest.mark.parametrize("values, expected",
                         [([1, 5, 3, 4, 2, 6], True),
                          ([1, 2, 3, 4, 5, 6], False),
                          ([2, 5, 9, 1, 6, 7, 3, 4, 8], True),
                          ([1, 2, 3, 4, 5, 6, 7, 8, 9], False)])
def test_is_magic_triangle(values, expected):
    result = is_magic_triangle(values)

    assert expected == result


@pytest.mark.parametrize("values, expected",
                         [([1, 5, 3, 4, 2, 6], True),
                          ([1, 2, 3, 4, 5, 6], False),
                          ([2, 5, 9, 1, 6, 7, 3, 4, 8], True),
                          ([1, 2, 3, 4, 5, 6, 7, 8, 9], False)])
def test_is_magic_triangle_v2(values, expected):
    result = is_magic_triangle_v2(values)

    assert expected == result
