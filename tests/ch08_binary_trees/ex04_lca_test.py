# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import pytest

from ch08_binary_trees.solutions.ex04_lca import create_lca_example_tree, find_lca


@pytest.mark.parametrize("value1, value2, expected",
                         [(1, 3, 2), (1, 5, 4), (2, 5, 4),
                          (3, 5, 4), (1, 7, 6)])
def test_find_lca(value1, value2, expected):
    root = create_lca_example_tree()

    result = find_lca(root, value1, value2)

    assert result.item == expected


def test_find_lca_special():
    root = create_lca_example_tree()

    result = find_lca(root, 1, 2)

    assert result.item == 2
