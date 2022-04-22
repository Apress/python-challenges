# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch05_datastructures.solutions.ex10_most_frequent_element import value_count, sort_dict_by_value


@pytest.mark.parametrize("values, expected",
                         [([1, 2, 3, 4, 4, 4, 3, 3, 2, 4],
                           {1: 1, 2: 2, 3: 3, 4: 4}),
                          ([1, 1, 1, 2, 2, 2, 3, 3, 3],
                           {1: 3, 2: 3, 3: 3})])
def test_value_count(values, expected):
    result = value_count(values)

    assert expected == result


@pytest.mark.parametrize("dictonary, expected",
                         [({1: 1, 2: 2, 3: 3, 4: 4},
                           {4: 4, 3: 3, 2: 2, 1: 1})])
def test_sort_dict_by_value(dictonary, expected):
    result = sort_dict_by_value(dictonary)

    assert expected == result
