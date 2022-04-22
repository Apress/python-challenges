# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch09_search_and_sort.solutions.ex06_quick_sort import quick_sort_inplace


@pytest.mark.parametrize("values, expected",
                         [([5, 2, 7, 1, 4, 3, 6, 8],
                           [1, 2, 3, 4, 5, 6, 7, 8]),
                          ([5, 2, 7, 9, 6, 3, 1, 4, 8],
                           [1, 2, 3, 4, 5, 6, 7, 8, 9]),
                          [[5, 2, 7, 9, 6, 3, 1, 4, 2, 3, 8],
                           [1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9]]])
def test_quick_sort_inplace(values, expected):
    quick_sort_inplace(values)

    assert values == expected






