# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch04_strings.solutions.ex03_reverse_string import reverse_inplace, reverse


def input_and_expected():
    return [("ABCD", "DCBA"), ("OTTO", "OTTO"), ("PETER", "RETEP")]

@pytest.mark.parametrize("input, expected",
                         input_and_expected())
def test_reverse(input, expected):
    assert reverse(input) == expected


@pytest.mark.parametrize("input, expected",
                         input_and_expected())
def test_reverse_inplace(input, expected):
    assert reverse_inplace(input) == expected




