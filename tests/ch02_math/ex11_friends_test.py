# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch02_math.solutions.ex11_friends import calc_friends


@pytest.mark.parametrize("max_exclusive, friends",
                         [(250, {220: 284}),
                          (300, {220: 284, 284: 220}),
                          (2_000, {220: 284, 284: 220,
                                   1_184: 1_210, 1_210: 1_184})])
def test_calc_friends(max_exclusive, friends):
    assert calc_friends(max_exclusive) == friends
