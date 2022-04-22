# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

from ch08_binary_trees.solutions.ex02_traverals_iterative import inorder_iterative, preorder_iterative, postorder_iterative
from ch08_binary_trees.intro import example_trees


def test_inorder_iterative():
    root = example_trees.create_example_tree()

    result = []
    inorder_iterative(root, lambda item: result.append(item))

    assert result == ["a1", "b2", "c3", "d4", "e5", "f6", "g7"]


def test_preorder_iterative():
    root = example_trees.create_example_tree()

    result = []
    preorder_iterative(root, lambda item: result.append(item))

    assert result == ["d4", "b2", "a1", "c3", "f6", "e5", "g7"]


def test_postorder_iterative():
    root = example_trees.create_example_tree()

    result = []
    postorder_iterative(root, lambda item: result.append(item))

    assert result == ["a1", "c3", "b2", "e5", "g7", "f6", "d4"]
