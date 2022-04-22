# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch04_strings.solutions.ex05_no_duplicate_chars import check_no_duplicate_chars, check_no_duplicate_chars_v2


def input_and_expected():
    return [("Otto", False), ("Adrian", False),
            ("Micha", True), ("ABCDEFG", True)]


@pytest.mark.parametrize("input, expected", input_and_expected())
def test_check_no_duplicate_chars(input, expected):
    assert check_no_duplicate_chars(input) == expected


@pytest.mark.parametrize("input, expected", input_and_expected())
def test_check_no_duplicate_chars_v2(input, expected):
    assert check_no_duplicate_chars_v2(input) == expected

