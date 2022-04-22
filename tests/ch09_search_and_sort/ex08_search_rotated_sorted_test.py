# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch09_search_and_sort.solutions.ex08_serach_rotated_sorted import find_flank_pos, binary_search_rotated, min_value, max_value


@pytest.mark.parametrize("values, expected",
                         [([25, 33, 47, 1, 2, 3, 5, 11], 3),
                          ([6, 7, 1, 2, 3, 4, 5], 2),
                          ([1, 2, 3, 4, 5, 6, 7], 0)])
def test_find_flank_pos(values, expected):
    flank_pos = find_flank_pos(values)

    assert flank_pos == expected


@pytest.mark.parametrize("values, search_for, expected",
                         [([25, 33, 47, 1, 2, 3, 5, 11], 47, 2),
                          ([25, 33, 47, 1, 2, 3, 5, 11], 3, 5),
                          ([25, 33, 47, 1, 2, 3, 5, 11], 13, -1),
                          ([1, 2, 3, 4, 5, 6, 7], 5, 4),
                          ([1, 2, 3, 4, 5, 6, 7], 13, -1)])
def test_binary_search_rotated(values, search_for, expected):
    pos = binary_search_rotated(values, search_for)

    assert pos == expected


@pytest.mark.parametrize("values, expected_min, expected_max",
                         [([25, 33, 47, 1, 2, 3, 5, 11], 1, 47),
                          ([6, 7, 1, 2, 3, 4, 5], 1, 7),
                          ([1, 2, 3, 4, 5, 6, 7], 1, 7)])
def test_min_max_value(values, expected_min, expected_max):
    min = min_value(values)
    max = max_value(values)

    assert min == expected_min and max == expected_max
