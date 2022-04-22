# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import unittest

import pytest
from parameterized import parameterized

from ch02_math.solutions.ex06_checksum import calc_checksum


class Ex06_CalcChecksum_Test(unittest.TestCase):

    @parameterized.expand([
        ("11111", 5), ("22222", 0), ("111111", 1),
        ("12345678", 4), ("87654321", 0)
    ])
    def test_calc_checksum(self, n, expected):
        result = calc_checksum(n)

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()


######################

## PYTEST
@pytest.mark.parametrize("n, expected",
                         [("11111", 5),
                          ("22222", 0),
                          ("111111", 1),
                          ("12345678", 4),
                          ("87654321", 0)])
def test_calc_checksum(n, expected):
    assert calc_checksum(n) == expected


def test_numberAsText_WrongInput():
    with pytest.raises(ValueError) as excinfo:
        calc_checksum("ABC")

    assert "illegal chars" in str(excinfo.value)
