# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch03_recursion.solutions.ex02_digits import count_digits, calc_sum_of_digits, calc_sum_of_digits_divmod, \
    count_digits_tricky, calc_sum_of_digits_shorter, count_digits_shorter


@pytest.mark.parametrize("number, expected", [(1234, 4), (1234567, 7)])
def test_count_digits(number, expected):
    assert count_digits(number) == expected


@pytest.mark.parametrize("number, expected", [(1234, 10), (1234567, 28)])
def test_calc_sum_of_digits(number, expected):
    assert calc_sum_of_digits(number) == expected


@pytest.mark.parametrize("number, expected", [(1234, 4), (1234567, 7)])
def test_count_digits_shorter(number, expected):
    assert count_digits_shorter(number) == expected


@pytest.mark.parametrize("number, expected", [(1234, 4), (1234567, 7)])
def test_count_digits_tricky(number, expected):
    assert count_digits_tricky(number) == expected


@pytest.mark.parametrize("number, expected", [(1234, 10), (1234567, 28)])
def test_calc_sum_of_digits_divmod(number, expected):
    assert calc_sum_of_digits_divmod(number) == expected


@pytest.mark.parametrize("number, expected", [(1234, 10), (1234567, 28)])
def test_calc_sum_of_digits_shorter(number, expected):
    assert calc_sum_of_digits_shorter(number) == expected


def test_calc_digits_wrong_input():
    with pytest.raises(ValueError) as excinfo:
        count_digits(-1)

    assert "value must be >= 0" in str(excinfo.value)


def test_calc_sum_of_digits_wrong_input():
    with pytest.raises(ValueError) as excinfo:
        calc_sum_of_digits(-1)

    assert "value must be >= 0" in str(excinfo.value)
