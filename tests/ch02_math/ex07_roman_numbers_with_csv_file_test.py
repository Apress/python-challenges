# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

import csv

from ch02_math.solutions.ex07_roman_numbers import from_roman_number, to_roman_number

def arabic_to_roman_number_map():
    result = []
    with open('arabicroman2.csv','rt') as file:
        data = csv.reader(file)

        skip_first = True
        for row in data:
            if not skip_first:
                result.append((int(row[0].strip()), row[1].strip()))
            skip_first = False

    return result


# Achtung hier andere Reihenfolge, damit man es nicht zweimal definieren muss
@pytest.mark.parametrize("expected, roman_number",
                         arabic_to_roman_number_map())
def test_from_roman_number(roman_number, expected):
    assert from_roman_number(roman_number) == expected


@pytest.mark.parametrize("roman_number, expected",
                         arabic_to_roman_number_map())
def test_to_roman_number(roman_number, expected):
    assert to_roman_number(roman_number) == expected
