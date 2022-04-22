# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch05_datastructures.solutions.ex11_list_add import list_add_improved, list_add_with_iter, list_add, \
    list_add_inverse


@pytest.mark.parametrize("values1, values2, expected",
                         [([1, 2, 3], [4, 5, 6], [5, 7, 9]),
                          ([9, 2, 7], [1, 3, 5], [1, 0, 6, 2])])
def test_list_add(values1, values2, expected):
    result = list_add(values1, values2)

    assert expected == result


@pytest.mark.parametrize("values1, values2, expected",
                         [([1, 2, 3], [4, 5, 6], [5, 7, 9]),
                          ([9, 2, 7], [1, 3, 5], [1, 0, 6, 2])])
def test_list_add_with_iter(values1, values2, expected):
    result = list_add_with_iter(values1, values2)

    assert expected == result


@pytest.mark.parametrize("values1, values2, expected",
                         [([1, 2, 3], [4, 5, 6], [5, 7, 9]),
                          ([9, 2, 7], [1, 3, 5], [1, 0, 6, 2])])
def test_list_add_improved(values1, values2, expected):
    result = list_add_improved(values1, values2)

    assert expected == result


@pytest.mark.parametrize("values1, values2, expected",
                         [([3, 2, 1], [6, 5, 4], [9, 7, 5]),
                          ([7, 2, 9], [5, 3, 1], [2, 6, 0, 1])])
def test_list_add_inverse(values1, values2, expected):
    result = list_add_inverse(values1, values2)

    assert expected == result
