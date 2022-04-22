# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest
import numpy as np

from ch06_arrays.solutions.ex03_palindrome import is_palindrome_rec, is_palindrome_iterative, is_palindrome_short


def values_and_expected():
    return [(["Ein", "Test", " -- ", "Test", "Ein"], True),
            (["Max", "Mike", "Mike", "Max"], True),
            (["Tim", "Tom", "Mike", "Max"], False)]


@pytest.mark.parametrize("values, expected", values_and_expected())
def test_is_palindrome_rec(values, expected):
    result = is_palindrome_rec(values)

    assert result == expected


@pytest.mark.parametrize("values, expected",
                         [(np.array(["Ein", "Test", " -- ", "Test", "Ein"]), True),
                          (np.array(["Max", "Mike", "Mike", "Max"]), True),
                          (np.array(["Tim", "Tom", "Mike", "Max"]), False)]
                         )
def test_is_palindrome_rec_using_np(values, expected):
    result = is_palindrome_rec(values)

    assert result == expected


@pytest.mark.parametrize("values, expected", values_and_expected())
def test_is_palindrome_iterative(values, expected):
    result = is_palindrome_iterative(values)

    assert result == expected


@pytest.mark.parametrize("values, expected", values_and_expected())
def test_is_palindrome_short(values, expected):
    result = is_palindrome_short(values)

    assert result == expected
