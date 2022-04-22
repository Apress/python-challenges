# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch07_recursion_advanced.solutions.ex08_all_palidrome_substrings import all_palindrome_parts_rec, \
    all_palindrome_parts_rec_optimized, all_palindrome_parts_rec_optimized_v3, longest_palindrome_part


def input_and_expected():
    return [("BCDEDCB",
             {"BCDEDCB", "CDEDC", "DED"}),
            ("ABALOTTOLL",
             {"ABA", "LL", "LOTTOL", "OTTO", "TT"}),
            ("racecar",
             {"aceca", "cec", "racecar"})]


@pytest.mark.parametrize("input, expected",
                         input_and_expected())
def test_all_palindrome_parts_recs(input, expected):
    result = all_palindrome_parts_rec(input)

    assert result == expected


@pytest.mark.parametrize("input, expected",
                         input_and_expected())
def test_all_palindrome_parts_recs_optimized(input, expected):
    result = all_palindrome_parts_rec_optimized(input)

    assert result == expected


@pytest.mark.parametrize("input, expected",
                         input_and_expected())
def test_all_palindrome_parts_recs_optimized_v3(input, expected):
    result = all_palindrome_parts_rec_optimized_v3(input)

    assert result == expected


@pytest.mark.parametrize("input, expected",
                         [("ABALOTTOLL", "LOTTOL"),
                          ("dreh_malam_herd", "dreh_malam_herd"),
                          ("abc_XYZYX_def", "_XYZYX_")])
def test_longest_palindrome(input, expected):
    longest = longest_palindrome_part(input)

    assert longest == expected
