# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch03_recursion.solutions.ex12_count_substrings import count_substrings, count_substrings_v2, \
    count_substrings_optimized


def create_inputs_and_expected():
    return [("xhixhix", "x", 3), ("xhixhix", "hi", 2), ("mic", "mic", 1),
            ("haha", "ho", 0), ("xxxxyz", "xx", 2), ("xxxx", "xx", 2),
            ("xx-xxx-xxxx-xxxxx-xxxxxx", "xx", 9),
            ("xx-xxx-xxxx-xxxxx-xxxxxx", "xxx", 5)]


@pytest.mark.parametrize("input, search_for, expected",
                         create_inputs_and_expected())
def test_count_substrings(input, search_for, expected):
    assert count_substrings(input, search_for) == expected


@pytest.mark.parametrize("input, search_for, expected",
                         [("xhixhix", "x", 3), ("xhixhix", "hi", 2),
                          ("mic", "mic", 1), ("haha", "ho", 0),
                          ("xxxxyz", "xx", 3), ("xxxx", "xx", 3),
                          ("xx-xxx-xxxx-xxxxx-xxxxxx", "xx", 15),
                          ("xx-xxx-xxxx-xxxxx-xxxxxx", "xxx", 10)])
def test_count_substrings_v2(input, search_for, expected):
    assert count_substrings_v2(input, search_for) == expected


@pytest.mark.parametrize("input, search_for, expected",
                         create_inputs_and_expected())
def test_count_substrings_optimized(input, search_for, expected):
    assert count_substrings_optimized(input, search_for) == expected
