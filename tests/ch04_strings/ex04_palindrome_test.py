# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch04_strings.solutions.ex04_palindrome import is_palindrome_rec, is_palindrome_special, is_palindrome, \
    is_palindrome_with_reverse, is_palindrome_special_with_reg_ex


def palindrome_inputs_and_expecteds():
    return [("Otto", True),
            ("ABCBX", False),
            ("ABCXcba", True)]


@pytest.mark.parametrize("input, expected",
                         palindrome_inputs_and_expecteds())
def test_is_palindrome(input, expected):
    assert is_palindrome(input) == expected


@pytest.mark.parametrize("input, expected",
                         palindrome_inputs_and_expecteds())
def test_is_palindrome_rec(input, expected):
    assert is_palindrome_rec(input) == expected


@pytest.mark.parametrize("input, expected",
                         [("Dreh mal am Herd.", True),
                          ("Das ist kein Palindrom!", False)])
def test_is_palindrome_special_on(input, expected):
    ignore_spaces_and_punctuation = True
    assert is_palindrome_special(input,
                                 ignore_spaces_and_punctuation) == expected


@pytest.mark.parametrize("input, expected",
                         [("Dreh mal am Herd.", False),
                          ("Das ist kein Palindrom!", False)])
def test_is_palindrome_special_off(input, expected):
    ignore_spaces_and_punctuation= False
    assert is_palindrome_special(input, ignore_spaces_and_punctuation) == expected


@pytest.mark.parametrize("input, expected",
                         [("Dreh mal am Herd.", True),
                          ("Das ist kein Palindrom!", False)])
def test_is_palindrome_special_reg_ex_on(input, expected):
    ignore_spaces_and_punctuation= True
    assert is_palindrome_special_with_reg_ex(input, ignore_spaces_and_punctuation) == expected



@pytest.mark.parametrize("input, expected",
                         palindrome_inputs_and_expecteds())
def test_is_palindrome_with_reverse(input, expected):
    assert is_palindrome_with_reverse(input) == expected
