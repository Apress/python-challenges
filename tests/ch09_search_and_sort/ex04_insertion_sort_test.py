# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

from ch09_search_and_sort.solutions.ex04_insertion_sort import insertion_sort


def test_insertion_sort():
    values = [7, 2, 5, 1, 6, 8, 9, 4, 3]
    insertion_sort(values)

    assert values == [1, 2, 3, 4, 5, 6, 7, 8, 9]

