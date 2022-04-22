# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch05_datastructures.solutions.ex06_longest_subsequence import find_longest_growing_sequence


@pytest.mark.parametrize("values, expected",
                         [([7, 2, 7, 1, 2, 5, 7, 1], [1, 2, 5, 7]),
                          ([7, 2, 7, 1, 2, 3, 8, 1, 2, 3, 4, 5],
                           [1, 2, 3, 4, 5]),
                          ([1, 1, 2, 2, 2, 3, 3, 3, 3],
                           [1, 1, 2, 2, 2, 3, 3, 3, 3]),
                          ([], [])])
def test_find_longest_growing_sequence(values, expected):
    result = find_longest_growing_sequence(values)

    assert expected == result
