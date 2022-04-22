# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch04_strings.solutions.ex10_anagram import is_anagram


@pytest.mark.parametrize("str1, str2, expected",
                         [("Otto", "Toto", True),
                          ("Mary", "Army", True),
                          ("Ananas", "Bananas", False)])
def test_is_anagram(str1, str2, expected):
    assert is_anagram(str1, str2) == expected
