# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch05_datastructures.solutions.ex05_maxrevenue import max_revenue_optimized, max_revenue


def prices_and_expected():
    return [([0, 10, 20, 30, 40, 50, 60, 70], 70),
            ([70, 60, 50, 40, 30, 20, 10], 0),
            ([], 0)]


@pytest.mark.parametrize("prices, expected",
                         prices_and_expected())
def test_max_revenue(prices, expected):
    result = max_revenue(prices)

    assert expected ==  result


@pytest.mark.parametrize("prices, expected",
                         prices_and_expected())
def test_max_revenue_optimized(prices, expected):
    result = max_revenue_optimized(prices)

    assert expected ==  result




