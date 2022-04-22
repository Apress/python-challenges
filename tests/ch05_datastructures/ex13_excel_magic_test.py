# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch05_datastructures.solutions.ex13_excel_magic import generate_following_values, generate_following_values_for_predefined


@pytest.mark.parametrize("start_value, sequence_length, expected",
                         [(1, 7, [1, 2, 3, 4, 5, 6, 7]),
                          (5, 4, [5, 6, 7, 8])])
def test_generate_following_values(start_value, sequence_length, expected):
    result = generate_following_values(start_value, sequence_length)

    assert expected == result


def predefined_values():
    return ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]


@pytest.mark.parametrize("predefined_values, current_value, "
                         "sequence_length, expected",
                         [(predefined_values(), "Monday", 3,
                           ["Monday", "Tuesday", "Wednesday"]),
                          (predefined_values(), "Friday", 8,
                           ["Friday", "Saturday", "Sunday", "Monday",
                            "Tuesday", "Wednesday", "Thursday", "Friday"])])
def test_generate_following_values_for_predefined(predefined_values,
                                                  current_value,
                                                  sequence_length, expected):
    result = generate_following_values_for_predefined(predefined_values,
                                                      current_value,
                                                      sequence_length)

    assert expected == result
