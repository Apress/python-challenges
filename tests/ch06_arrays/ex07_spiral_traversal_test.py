# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch06_arrays.solutions.ex07_spiral_traversal import spiral_traversal
from ch06_arrays.solutions.ex07_spiral_traversal_optimized import spiral_traversal_optimized


def values_and_expected():
    return [([["A", "B", "C", "D"],
              ["J", "K", "L", "E"],
              ["I", "H", "G", "F"]],
             list("ABCDEFGHIJKL")),
            ([[1, 2, 3, 4],
              [12, 13, 14, 5],
              [11, 16, 15, 6],
              [10, 9, 8, 7]],
             [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])]


@pytest.mark.parametrize("values, expected", values_and_expected())
def test_spiral_traversal(values, expected):
    result = spiral_traversal(values)

    assert result == expected


@pytest.mark.parametrize("values, expected", values_and_expected())
def test_spiral_traversal_optimized(values, expected):
    result = spiral_traversal_optimized(values)

    assert result == expected

