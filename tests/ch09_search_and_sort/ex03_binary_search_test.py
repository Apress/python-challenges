# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch09_search_and_sort.solutions.ex03_binary_search import binary_search, binary_search_iterative, binary_search_optimized


@pytest.mark.parametrize("sorted_values, search_for, expected",
                         [([1, 2, 3, 4, 5, 7, 8, 9], 5, True),
                          ([1, 2, 3, 4, 5, 7, 8, 9], 6, False)])
def test_binary_search(sorted_values, search_for, expected):
    assert binary_search(sorted_values, search_for) == expected


@pytest.mark.parametrize("sorted_values, search_for, expected",
                         [([1, 2, 3, 4, 5, 7, 8, 9], 5, True),
                          ([1, 2, 3, 4, 5, 7, 8, 9], 6, False)])
def test_binary_search_optimized(sorted_values, search_for, expected):
    assert binary_search_optimized(sorted_values, search_for) == expected


@pytest.mark.parametrize("sorted_values, search_for, expected",
                         [([1, 2, 3, 4, 5, 7, 8, 9], 5, 4),
                          ([1, 2, 3, 4, 5, 7, 8, 9], 6, -1)])
def test_binary_search_iterative(sorted_values, search_for, expected):
    assert binary_search_iterative(sorted_values, search_for) == expected
