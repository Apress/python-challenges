# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch03_recursion.solutions.ex04_reverse_string import reverse_string


@pytest.mark.parametrize("input, expected",
                         [("A", "A"), ("ABC", "CBA"),
                          ("abcdefghi", "ihgfedcba")])
def test_reverse_string(input, expected):
    assert reverse_string(input) == expected

