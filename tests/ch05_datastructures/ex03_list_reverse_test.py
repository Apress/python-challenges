# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch05_datastructures.solutions.ex03_list_reverse import reverse, reverse_inplace, reverse_with_slicing


def list_reverse_inputs_and_expected():
    return [([1, 2, 3, 4], [4, 3, 2, 1]),
            (["A", "BB", "CCC", "DDDD"], ["DDDD", "CCC", "BB", "A"])]


@pytest.mark.parametrize("inputs, expected",
                         list_reverse_inputs_and_expected())
def test_reverse(inputs, expected):
    result = reverse(inputs)

    assert expected == result


@pytest.mark.parametrize("inputs, expected",
                         list_reverse_inputs_and_expected())
def test_reverse_inplace(inputs, expected):
    modifiable_inputs = list(inputs)

    reverse_inplace(modifiable_inputs)

    assert modifiable_inputs == expected


@pytest.mark.parametrize("inputs, expected",
                         list_reverse_inputs_and_expected())
def test_reverse_with_slicing(inputs, expected):
    result = reverse_with_slicing(inputs)

    assert expected == result
