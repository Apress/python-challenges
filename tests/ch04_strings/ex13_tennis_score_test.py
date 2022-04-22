# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch04_strings.solutions.ex13_tennis_score import tennis_score


@pytest.mark.parametrize("score, expected",
                         [("1:0", "Fifteen Love"),
                          ("2:2", "Thirty Thirty"),
                          ("2:3", "Thirty Forty"),
                          ("3:3", "Deuce"),
                          ("4:3", "Advantage Micha"),
                          ("4:4", "Deuce"),
                          ("5:4", "Advantage Micha"),
                          ("6:4", "Game Micha")])
def test_tennis_score_hard_win(score, expected):
    assert tennis_score(score, "Micha", "Tim") == expected


@pytest.mark.parametrize("score, expected",
                         [("1:0", "Fifteen Love"),
                          ("2:2", "Thirty Thirty"),
                          ("3:2", "Forty Thirty"),
                          ("4:2", "Game Micha")])
def test_tennis_score_normal_win(score, expected):
    assert tennis_score(score, "Micha", "Tim") == expected


@pytest.mark.parametrize("score, expected",
                         [("1:0", "Fifteen Love"),
                          ("2:0", "Thirty Love"),
                          ("3:0", "Forty Love"),
                          ("4:0", "Game Micha")])
def test_tennis_score_straight_win(score, expected):
    assert tennis_score(score, "Micha", "Tim") == expected
