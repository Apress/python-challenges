# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch04_strings.solutions.ex02_join import join


@pytest.mark.parametrize("values, delimiter, expected",
                         [(["hello", "world", "message"], " +++ ",
                           "hello +++ world +++ message"),
                          (["Micha", "Zürich"], " likes ",
                           "Micha likes Zürich")])
def test_join(values, delimiter, expected):
    assert join(values, delimiter) == expected
