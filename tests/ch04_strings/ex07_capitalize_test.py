# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch04_strings.solutions.ex07_capitalize import capitalize, capitalize_words, capitalize_special_2


@pytest.mark.parametrize("input, expected",
                         [("this is a very special title",
                           "This Is A Very Special Title"),
                          ("effective java is great",
                           "Effective Java Is Great")])
def test_capitalize(input, expected):
    assert capitalize(input) == expected


@pytest.mark.parametrize("words, expected",
                         [(["this", "is", "a", "very", "special", "title"],
                           ["This", "Is", "A", "Very", "Special", "Title"]),
                          (["effective", "java", "is", "great"],
                           ["Effective", "Java", "Is", "Great"])])
def test_capitalize_words(words, expected):
    assert capitalize_words(words) == expected


@pytest.mark.parametrize("words, expected",
                         [(["this", "is", "a", "very", "special", "title"],
                           ["This", "is", "a", "Very", "Special", "Title"]),
                          (["effective", "java", "is", "great"],
                           ["Effective", "Java", "is", "Great"])])
def test_capitalize_special_2(words, expected):
    assert capitalize_special_2(words, ["a", "is"]) == expected
