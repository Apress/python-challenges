# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch04_strings.solutions.ex01_number_conversions import is_binary_number, binary_to_decimal, hex_to_decimal, \
    is_binary_number_v2


@pytest.mark.parametrize("value, expected",
                         [("10101", True),
                          ("222", False),
                          ("12345", False)])
def test_is_binary_number(value, expected):
    assert is_binary_number(value) == expected


@pytest.mark.parametrize("value, expected",
                         [("10101", True),
                          ("222", False),
                          ("12345", False)])
def test_is_binary_number_v2(value, expected):
    assert is_binary_number_v2(value) == expected


@pytest.mark.parametrize("value, expected",
                         [("111", 7), ("1010", 10),
                          ("1111", 15), ("10000", 16)])
def test_binary_to_decimal(value, expected):
    assert binary_to_decimal(value) == expected


@pytest.mark.parametrize("value, expected",
                         [("7", 7), ("A", 10),
                          ("F", 15), ("10", 16)])
def test_hex_to_decimal(value, expected):
    assert hex_to_decimal(value) == expected
