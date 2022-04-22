# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch06_arrays.solutions.ex11_array_min_max_and_pos import find_min, find_max, find_min_pos, find_max_pos


def test_find_min_and_max():
    values = [ 2, 3, 4, 5, 6, 7, 8, 9, 1, 10 ]

    assert find_min(values) == 1
    assert find_max(values) == 10


@pytest.mark.parametrize("lower, upper, expected_pos, expected_value",
                         [(0, 10, 8, 1), (2, 7, 3, 2), (0, 7, 3, 2)])
def test_find_min_pos(lower, upper, expected_pos, expected_value):
    values = [ 5, 3, 4, 2, 6, 7, 8, 9, 1, 10 ]

    result_pos = find_min_pos(values, lower, upper)

    assert expected_pos == result_pos
    assert expected_value == values[result_pos]


@pytest.mark.parametrize("lower, upper, expected_pos, expected_value",
                         [(0, 10, 9, 49), (2, 7, 5, 10), (0, 7, 1, 22)])
def test_find_max_pos(lower, upper, expected_pos, expected_value):
    values = [ 1, 22, 3, 4, 5, 10, 7, 8, 9, 49 ]

    result_pos = find_max_pos(values, lower, upper)

    assert expected_pos == result_pos
    assert expected_value == values[result_pos]

