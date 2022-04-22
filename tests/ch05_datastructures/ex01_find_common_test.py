# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch05_datastructures.solutions.ex01_find_common import find_common, find_common_short


def inputs_and_expected():
    return [([1, 2, 4, 7, 8], [2, 3, 7, 9], {2, 7}),
            ([1, 2, 7, 4, 7, 8], [7, 7, 3, 2, 9], {2, 7}),
            ([2, 4, 6, 8], [1, 3, 5, 7, 9], set())]


@pytest.mark.parametrize("values1, values2, expected",
                         inputs_and_expected())
def test_find_common(values1, values2, expected):
    result = find_common(values1, values2)

    assert expected == result


@pytest.mark.parametrize("values1, values2, expected",
                         inputs_and_expected())
def test_find_common(values1, values2, expected):
    result = find_common_short(values1, values2)

    assert expected == result



