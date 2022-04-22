# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch03_recursion.solutions.ex07_convert import to_binary, to_octal, to_hex


@pytest.mark.parametrize("value, expected",
                         [(5, "101"), (7, "111"), (22, "10110"),
                          (42, "101010"), (256, "100000000")])
def test_to_binary(value, expected):
    assert to_binary(value) == expected


@pytest.mark.parametrize("value, expected",
                         [(42, "52"), (7, "7"), (8, "10")])
def test_to_octal(value, expected):
    assert to_octal(value) == expected


@pytest.mark.parametrize("value, expected",
                         [(77, "4D"), (15, "F"), (16, "10")])
def test_to_hex(value, expected):
    assert to_hex(value) == expected

