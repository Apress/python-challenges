# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch04_strings.solutions.ex15_str_to_number import str_to_number, str_to_number_bonus


@pytest.mark.parametrize("input, expected",
                         [("+123", 123), ("-123", -123),
                          ("123", 123), ("7271", 7271)])
def test_str_to_number(input, expected):
    assert str_to_number(input) == expected


def test_str_to_number_invalid_input():
    with pytest.raises(ValueError):
        str_to_number("ABC")



@pytest.mark.parametrize("input, expected",
                         [("+123", 123), ("-123", -123),
                          ("123", 123), ("7271", 7271),
                          ("+0o77", 63), ("-0o77", -63),
                          ("0o77", 63), ("+0o123", 83),
                          ("-0o123", -83), ("0o123", 83)])
def test_str_to_number_bonus(input, expected):
    assert str_to_number_bonus(input) == expected


def test_str_to_number_bonus_invalid_input():
    with pytest.raises(ValueError) as excinfo:
        str_to_number_bonus("0o128")

    assert str(excinfo.value).find("found digit >= 8") != -1

