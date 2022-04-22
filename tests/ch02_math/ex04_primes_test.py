# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import unittest

import pytest
from parameterized import parameterized

from ch02_math.solutions.ex04_primes import calc_primes_up_to, is_prime, calc_primes_up_to_v2


class Ex04PrimesTest(unittest.TestCase):

    @parameterized.expand([
        (10, [2, 3, 5, 7]),
        (15, [2, 3, 5, 7, 11, 13]),
        (20, [2, 3, 5, 7, 11, 13, 17, 19]),
        (25, [2, 3, 5, 7, 11, 13, 17, 19, 23]),
        (50, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
    ])
    def test_calc_primes_up_to(self, n, expected):
        result = calc_primes_up_to(n)

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()


######################

## PYTEST
def input_and_expected():
    return [(2, [2]),
            (3, [2, 3]),
            (10, [2, 3, 5, 7]),
            (15, [2, 3, 5, 7, 11, 13]),
            (20, [2, 3, 5, 7, 11, 13, 17, 19]),
            (25, [2, 3, 5, 7, 11, 13, 17, 19, 23]),
            (50, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])]


@pytest.mark.parametrize("n, expected",
                         input_and_expected())
def test_calc_primes_up_to(n, expected):
    assert calc_primes_up_to(n) == expected


@pytest.mark.parametrize("n, expected",
                         input_and_expected())
def test_calc_primes_up_to_v2(n, expected):
    assert calc_primes_up_to_v2(n) == expected



@pytest.mark.parametrize("n, expected",
                         [(2, True),
                          (3, True),
                          (4, False),
                          (5, True),
                          (6, False),
                          (7, True)])
def test_is_prime(n, expected):
    assert is_prime(n) == expected
