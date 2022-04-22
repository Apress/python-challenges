# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch07_recursion_advanced.solutions.ex03_lcs import lcs, lcs_optimized, lcs_from_start


@pytest.mark.parametrize("value1, value2, expected",
                         [("ABCE", "ZACEF", "ACE"),
                          ("ABCXY", "XYACB", "AB"),
                          ("ABCMIXCHXAEL", "MICHAEL", "MICHAEL")])
def test_lcs(value1, value2, expected):
    result = lcs(value1, value2)

    assert result == expected


@pytest.mark.parametrize("value1, value2, expected",
                         [("ABCE", "ZACEF", "ACE"),
                          ("ABCXY", "XYACB", "XY"),
                          ("ABCMIXCHXAEL", "MICHAEL", "MICHAEL")])
def test_lcs_from_start(value1, value2, expected):
    result = lcs_from_start(value1, value2)

    assert result == expected


@pytest.mark.parametrize("value1, value2, expected",
                         [("ABCE", "ZACEF", "ACE"),
                          ("ABCXY", "XYACB", "AB"),
                          ("ABCMIXCHXAEL", "MICHAEL", "MICHAEL")])
def test_lcs_optimized(value1, value2, expected):
    result = lcs_optimized(value1, value2)

    assert result == expected
