# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch04_strings.solutions.ex06_remove_duplicates import remove_duplicates


@pytest.mark.parametrize("input, expected",
                         [("bananas", "bans"),
                          ("lalalamama", "lam"),
                          ("MICHAEL", "MICHAEL") ])
def test_remove_duplicates(input, expected):
    assert remove_duplicates(input) == expected

