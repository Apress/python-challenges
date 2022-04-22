# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch03_recursion.solutions.ex11_permutations import calc_permutations, calc_permutations_mini_opt, \
    calc_permutations_built_in


def input_and_expected():
    return [("A", {"A"}),
            ("AA", {"AA"}),
            ("AB", {"AB", "BA"}),
            ("ABC", {"ABC", "BAC", "ACB", "CAB", "CBA", "BCA"}),
            ("AAC", {"AAC", "ACA", "CAA"})]


@pytest.mark.parametrize("input, expected", input_and_expected())
def test_calc_permutations(input, expected):
    assert calc_permutations(input) == expected


@pytest.mark.parametrize("input, expected", input_and_expected())
def test_calc_permutations_mini_opt(input, expected):
    assert calc_permutations_mini_opt(input) == expected


@pytest.mark.parametrize("input, expected", input_and_expected())
def test_calc_permutations_built_in(input, expected):
    assert calc_permutations_built_in(input) == expected
