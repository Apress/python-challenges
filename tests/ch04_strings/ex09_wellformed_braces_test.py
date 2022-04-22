# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch04_strings.solutions.ex09_wellformed_braces import check_braces


@pytest.mark.parametrize("input, expected, hint",
                         [("(())", True, "ok"),
                          ("()()", True, "ok"),
                          ("(()))((())", False, "nicht sauber geschachtelt"),
                          ("(()", False, "keine passende Klammerung"),
                          (")()", False, "startet mit schliessender Klammer")])
def test_check_braces(input, expected, hint):
    assert check_braces(input) == expected
