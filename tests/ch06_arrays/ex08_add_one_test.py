# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch06_arrays.solutions.ex08_add_one import add_one


def values_and_expected():
    return [([1, 3, 2, 4], [1, 3, 2, 5]),
            ([1, 4, 8, 9], [1, 4, 9, 0]),
            ([1, 3, 9, 9], [1, 4, 0, 0]),
            ([9, 9, 9, 9], [1, 0, 0, 0, 0])]


@pytest.mark.parametrize("values, expected", values_and_expected())
def test_add_one(values, expected):
    result = add_one(values)

    assert result == expected
