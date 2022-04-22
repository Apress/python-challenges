# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch08_binary_trees.solutions.ex05_levelorder import levelorder
from ch08_binary_trees.solutions.ex08_reconstruct import reconstruct, reconstruct_clearer


def test_reconstruct_from_list():
    inputs = [1, 2, 3, 4, 5, 6, 7]

    result_root = reconstruct(inputs)
    result = convert_to_list(result_root)

    assert result == [4, 2, 6, 1, 3, 5, 7]


@pytest.mark.parametrize("preorder_values, inorder_values, expected",
                         [([4, 2, 1, 3, 6, 5, 7], [1, 2, 3, 4, 5, 6, 7],
                           [4, 2, 6, 1, 3, 5, 7]),
                          ([5, 4, 2, 1, 3, 7, 6, 8], [1, 2, 3, 4, 5, 6, 7, 8],
                           [5, 4, 7, 2, 6, 8, 1, 3])])
def test_reconstruct_from_pre_in_order(preorder_values,
                                       inorder_values, expected):

    result_root = reconstruct_clearer(preorder_values, inorder_values)
    result = convert_to_list(result_root)

    assert result == expected


def convert_to_list(node):
    result = []
    levelorder(node, lambda item: result.append(item))
    return result
