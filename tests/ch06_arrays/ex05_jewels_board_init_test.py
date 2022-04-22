# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import numpy as np

from ch06_arrays.solutions.ex05_jewels_board_init import check_board_validity


def test_check_board_validity_with_conflicts():
    values_with_errors = [[2, 3, 3, 4, 4, 3, 2],
                          [1, 3, 3, 1, 3, 4, 4],
                          [4, 1, 4, 3, 3, 1, 3],
                          [2, 2, 1, 1, 2, 3, 2],
                          [3, 2, 4, 4, 3, 3, 4]]

    array_with_errors = np.array(values_with_errors)

    errors1 = check_board_validity(values_with_errors)
    errors2 = check_board_validity(array_with_errors)

    assert errors1 == errors2 and len(errors1) == 3


def test_check_board_validity_no_conflicts():
    values = [[2, 3, 3, 4, 4, 3, 2],
              [1, 3, 3, 1, 3, 4, 4],
              [4, 1, 4, 5, 3, 1, 3],
              [2, 2, 5, 1, 2, 3, 2],
              [3, 2, 4, 4, 5, 3, 4]]

    errors = check_board_validity(values)

    assert errors == []
