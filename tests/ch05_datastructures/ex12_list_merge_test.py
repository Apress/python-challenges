# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch05_datastructures.solutions.ex12_list_merge import merge, merge_with_iter


def inputs_and_expected():
    return [([1, 4, 7, 12, 20], [10, 15, 17, 33],
             [1, 4, 7, 10, 12, 15, 17, 20, 33]),
            ([2, 3, 5, 7], [11, 13, 17],
             [2, 3, 5, 7, 11, 13, 17]),
            ([2, 3, 5, 7, 11], [7, 11, 13, 17],
             [2, 3, 5, 7, 7, 11, 11, 13, 17]),
            ([1, 2, 3], [],
             [1, 2, 3])]


@pytest.mark.parametrize("values1, values2, expected",
                         inputs_and_expected())
def test_merge(values1, values2, expected):
    result = merge(values1, values2)

    assert expected == result


@pytest.mark.parametrize("values1, values2, expected",
                         inputs_and_expected())
def test_merge_with_iter(values1, values2, expected):
    result = merge_with_iter(values1, values2)

    assert expected == result

