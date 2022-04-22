# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

from ch06_arrays.solutions.ex02_flip import flip_horizontally, flip_vertically, flip_horizontally_v2, \
    flip_vertically_just_for_lists


def test_flip_horizontally():
    hori_values = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]

    flip_horizontally(hori_values)

    expected = [[3, 2, 1],
                [6, 5, 4],
                [9, 8, 7]]

    assert hori_values == expected


def test_flip_vertically():
    vert_values = [[1, 1, 4, 4],
                   [2, 2, 5, 5],
                   [3, 3, 6, 6]]

    flip_vertically(vert_values)

    expected = [[3, 3, 6, 6],
                [2, 2, 5, 5],
                [1, 1, 4, 4]]

    assert vert_values == expected


def test_flip_horizontally_v2():
    hori_values = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]

    flip_horizontally_v2(hori_values)

    expected = [[3, 2, 1],
                [6, 5, 4],
                [9, 8, 7]]

    assert hori_values == expected


def test_flip_vertically_just_for_lists():
    vert_values = [[1, 1, 4, 4],
                   [2, 2, 5, 5],
                   [3, 3, 6, 6]]

    flip_vertically_just_for_lists(vert_values)

    expected = [[3, 3, 6, 6],
                [2, 2, 5, 5],
                [1, 1, 4, 4]]

    assert vert_values == expected
