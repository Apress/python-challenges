# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch06_arrays.solutions.ex13_minesweeper import calc_bomb_count


# Verstecken der Randfeld - Logik und der Konvertierung
def to_bool_array(bombs):
    width = len(bombs[0])
    height = len(bombs)

    result = [[False for _ in range(width + 2)] for _ in range(height + 2)]

    for y in range(height):
        for x in range(width):
            if bombs[y][x] == '*':
                result[y + 1][x + 1] = True

    return result


def to_int_array(values):
    width = len(values[0])
    height = len(values)

    result = [[0 for _ in range(width + 2)] for _ in range(height + 2)]

    for y in range(height):
        for x in range(width):
            current_char = values[y][x]
            if current_char == 'B':
                result[y + 1][x + 1] = 9
            else:
                result[y + 1][x + 1] = int(current_char)

    return result


def create_bomb_array_and_expected():
    bombs1 = ["*..",
              "..*",
              "..*"]

    result1 = ["B21",
               "13B",
               "02B"]

    bombs2 = [".**..",
              "*.**.",
              "**...",
              "*..*.",
              "***.."]

    result2 = ["2BB31",
               "B6BB1",
               "BB432",
               "B64B1",
               "BBB21"]

    return [(to_bool_array(bombs1), to_int_array(result1)),
            (to_bool_array(bombs2), to_int_array(result2))]


@pytest.mark.parametrize("bombs, expected", create_bomb_array_and_expected())
def test_calc_bomb_count(bombs, expected):
    result = calc_bomb_count(bombs)

    assert result == expected
