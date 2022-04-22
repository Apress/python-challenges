# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest


from ch04_strings.solutions.ex11_morse_code import to_morse_code


@pytest.mark.parametrize("input, expected",
                         [("SOS", ". . .   - - -   . . ."),
                          ("TWEET", "-   . - -   .   .   -"),
                          ("OST", "- - -   . . .   -"),
                          ("WEST", ". - -   .   . . .   -")])
def test_to_morse_code(input, expected):
    assert to_morse_code(input) == expected
