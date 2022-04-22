# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch06_arrays.solutions.ex10_flood_fill import flood_fill


def create_world_and_expected_fills():
    first_world = [list("   #  "),
                   list("    # "),
                   list("#   # "),
                   list(" # #  "),
                   list("  #   ")]

    first_filled = [list("***#  "),
                    list("****# "),
                    list("#***# "),
                    list(" #*#  "),
                    list("  #   ")]

    second_world = [list("   #      # "),
                    list("    #      #"),
                    list("#   #     # "),
                    list(" # #     #  "),
                    list("  #     #   ")]

    second_filled = [list("   #******# "),
                     list("    #******#"),
                     list("#   #*****# "),
                     list(" # #*****#  "),
                     list("  #*****#   ")]

    return [(first_world, first_filled, 0, 0,),
            (second_world, second_filled, 4, 4)]


@pytest.mark.parametrize("world, expected, start_x, start_y",
                         create_world_and_expected_fills())
def test_flood_fill(world, expected, start_x, start_y):
    flood_fill(world, start_x, start_y)

    assert world == expected


def generate_pattern():
    return [list(".|."),
            list("-*-"),
            list(".|.")]


def generate_pattern_2():
    return [list("---"),
            list("~~~"),
            list("===")]


def generate_big_world():
    return [list("           #   |     "),
            list("       ##   #   |    "),
            list("    #####    #   __  "),
            list("       ###   #     | "),
            list(" ###    #    #      |"),
            list("    #   #    #     | "),
            list("     # #    #    --  "),
            list("      #    #    |    ")]
