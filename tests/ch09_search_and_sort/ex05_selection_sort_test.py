# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

from ch09_search_and_sort.solutions.ex05_selection_sort import selection_sort_max_inplace


def test_selection_sort_max_inplace():
    values = [7, 2, 5, 1, 6, 8, 9, 4, 3]
    selection_sort_max_inplace(values)

    assert values == [1, 2, 3, 4, 5, 6, 7, 8, 9]

