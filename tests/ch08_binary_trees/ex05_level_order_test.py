# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

from ch08_binary_trees.solutions.ex05_levelorder import levelorder, create_level_order_example_tree


def test_levelorder():
    root = create_level_order_example_tree()

    result = []
    levelorder(root, lambda item: result.append(item))

    assert result == ["1", "2", "3", "4", "5", "6", "7"]
