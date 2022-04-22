# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch09_search_and_sort.solutions.ex07_bucket_sort import bucket_sort


@pytest.mark.parametrize("values, max, expected",
                         [([10, 50, 22, 7, 42, 111, 50, 7], 150,
                           [7, 7, 10, 22, 42, 50, 50, 111]),
                          ([10, 50, 22, 7, 42, 111, 50, 7], 120,
                           [7, 7, 10, 22, 42, 50, 50, 111]),
                          [[5, 2, 7, 9, 6, 3, 1, 4, 2, 3, 8], 10,
                           [1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9]]])
def test_bucket_sort(values, max, expected):
    result = bucket_sort(values, max)

    assert result == expected
