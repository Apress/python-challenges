# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch05_datastructures.solutions.ex04_remove_duplicates import remove_duplicates, remove_duplicates_with_dict


def inputs_and_expected():
    return [([1, 1, 2, 3, 4, 1, 2, 3], [1, 2, 3, 4]),
            ([7, 5, 3, 5, 1], [7, 5, 3, 1]),
            ([1, 1, 1, 1], [1])]


@pytest.mark.parametrize("inputs, expected",
                         inputs_and_expected())
def test_remove_duplicates(inputs, expected):
    result = remove_duplicates(inputs)

    assert expected == result


@pytest.mark.parametrize("inputs, expected",
                         inputs_and_expected())
def test_remove_duplicates_with_dict(inputs, expected):
    result = remove_duplicates_with_dict(inputs)

    assert expected == result

