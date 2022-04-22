# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch07_recursion_advanced.solutions.ex06_math_operations import find_all_combinations, all_combinations_with_value


@pytest.mark.parametrize("digits,  expected",
                         [([1, 2, 3],
                           {"12-3": 9,
                            "123": 123,
                            "1+2+3": 6,
                            "1+2-3": 0,
                            "1-2+3": 2,
                            "1-23": -22,
                            "1-2-3": -4,
                            "1+23": 24,
                            "12+3": 15})])
def test_all_combinations(digits, expected):
    result = find_all_combinations(digits)

    assert result == expected


@pytest.mark.parametrize("digits, value, expected",
                         [([1, 2, 3, 4, 5, 6, 7, 8, 9], 100,
                           {"1+23-4+5+6+78-9",
                            "12+3+4+5-6-7+89",
                            "123-45-67+89",
                            "123+4-5+67-89",
                            "123-4-5-6-7+8-9",
                            "123+45-67+8-9",
                            "1+2+3-4+5+6+78+9",
                            "12+3-4+5+67+8+9",
                            "1+23-4+56+7+8+9",
                            "1+2+34-5+67-8+9",
                            "12-3-4+5-6+7+89"})])
def test_all_combinations_with_value(digits, value, expected):
    result = all_combinations_with_value(digits, value)

    assert result == expected
