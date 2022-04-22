# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

## PYTEST
from ch02_math.solutions.ex07_roman_numbers import from_roman_number, to_roman_number


def arabic_to_roman_number_map():
    return [(1, "I"), (2, "II"), (3, "III"), (4, "IV"),
            (5, "V"), (7, "VII"), (9, "IX"), (17, "XVII"),
            (40, "XL"), (90, "XC"), (400, "CD"), (444, "CDXLIV"),
            (500, "D"), (900, "CM"), (1000, "M"), (1666, "MDCLXVI"),
            (1971, "MCMLXXI"), (2018, "MMXVIII"), (2019, "MMXIX"),
            (2020, "MMXX"), (3000, "MMM")]

# Achtung hier andere Reihenfolge, damit man es nicht zweimal definieren muss
@pytest.mark.parametrize("expected, roman_number",
                         arabic_to_roman_number_map())
def test_from_roman_number(roman_number, expected):
    assert from_roman_number(roman_number) == expected


@pytest.mark.parametrize("roman_number, expected",
                         arabic_to_roman_number_map())
def test_to_roman_number(roman_number, expected):
    assert to_roman_number(roman_number) == expected
