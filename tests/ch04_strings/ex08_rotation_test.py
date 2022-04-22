# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch04_strings.solutions.ex08_rotation import contains_rotation


@pytest.mark.parametrize("str1, str2, expected",
                         [("ABCD", "ABC", True),
                          ("ABCDEF", "EFAB", True),
                          ("BCDE", "EC", False),
                          ("Challenge", "GECH", True)])
def test_contains_rotation(str1, str2, expected):
    assert contains_rotation(str1, str2) == expected
