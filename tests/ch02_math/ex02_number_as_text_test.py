# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import unittest

import pytest
from parameterized import parameterized

from ch02_math.solutions.ex02_number_as_text import number_as_text


class Ex02_NumberAsText_Test(unittest.TestCase):
    @parameterized.expand([
        (7, "SEVEN"), (42, "FOUR TWO"),
        (7271, "SEVEN TWO SEVEN ONE"),
        (24680, "TWO FOUR SIX EIGHT ZERO"),
        (13579, "ONE THREE FIVE SEVEN NINE")
    ])
    def test_number_as_text(self, n, expected):
        result = number_as_text(n)

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()


## PYTEST
@pytest.mark.parametrize("n, expected",
                         [(7, "SEVEN"), (42, "FOUR TWO"),
                          (7271, "SEVEN TWO SEVEN ONE"),
                          (24680, "TWO FOUR SIX EIGHT ZERO"),
                          (13579, "ONE THREE FIVE SEVEN NINE")])
def test_number_as_text(n, expected):
    assert number_as_text(n) == expected
