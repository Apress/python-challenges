# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

## PYTEST
from ch02_math.solutions.ex12_primefactors import calc_prime_factors, calc_prime_factors_optimized


def value_and_prime_factors():
    return [(8, [2, 2, 2]),
            (14, [2, 7]),
            (42, [2, 3, 7]),
            (1155, [3, 5, 7, 11]),
            (2222, [2, 11, 101])]

@pytest.mark.parametrize("value, primefactors",
                         value_and_prime_factors())
def test_calc_prime_factors(value, primefactors):
    assert calc_prime_factors(value) == primefactors

@pytest.mark.parametrize("value, primefactors",
                         value_and_prime_factors())
def test_calc_prime_factors_optimized(value, primefactors):
    assert calc_prime_factors_optimized(value) == primefactors
