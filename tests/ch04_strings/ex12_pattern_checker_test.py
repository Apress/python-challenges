# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch04_strings.solutions.ex12_pattern_checker import matches_pattern


@pytest.mark.parametrize("pattern, input, expected",
                         [("x", "", False),
                          ("", "x", False)])
def test_matches_pattern_special_cases(pattern, input, expected):
    assert matches_pattern(pattern, input) == expected


@pytest.mark.parametrize("pattern, input, expected",
                         [("xyyx", "tim mike mike tim", True),
                          ("xyyx", "time mike tom tim", False),
                          ("xyxx", "tim mike mike tim", False),
                          ("xxxx", "tim tim tim tim", True)])
def test_matches_pattern(pattern, input, expected):
    assert matches_pattern(pattern, input) == expected
