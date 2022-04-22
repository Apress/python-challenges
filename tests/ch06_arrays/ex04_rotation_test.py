# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

from ch06_arrays.solutions.ex04_rotate_inplace import rotate_inplace


def test_rotation():
    values = [['1', '2', '3', '4', '5', '6'],
              ['J', 'K', 'L', 'M', 'N', '7'],
              ['I', 'V', 'W', 'X', 'O', '8'],
              ['H', 'U', 'Z', 'Y', 'P', '9'],
              ['G', 'T', 'S', 'R', 'Q', '0'],
              ['F', 'E', 'D', 'C', 'B', 'A']]

    rotate_inplace(values)

    expected = [to_list("F G H I J 1"),
                to_list("E T U V K 2"),
                to_list("D S Z W L 3"),
                to_list("C R Y X M 4"),
                to_list("B Q P O N 5"),
                # so sähe es von Hand aus
                list("A 0 9 8 7 6".replace(" ", ""))]

    assert values == expected


def to_list(text):
    return list(text.replace(" ", ""))
