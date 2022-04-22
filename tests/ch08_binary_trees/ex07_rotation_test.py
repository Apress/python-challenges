# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

from ch08_binary_trees.solutions.ex05_levelorder import levelorder
from ch08_binary_trees.solutions.ex07_rotation import rotate_left, rotate_right
from ch08_binary_trees.intro import example_trees


def test_rotate_left():
    root = example_trees.create_example_tree()

    result = rotate_left(root)
    as_list = convert_to_list(result)
    assert as_list == ["f6", "d4", "g7", "b2", "e5", "a1", "c3"]


def test_rotate_right():
    root = example_trees.create_example_tree()

    result = rotate_right(root)
    as_list = convert_to_list(result)
    assert as_list == ["b2", "a1", "d4", "c3", "f6", "e5", "g7"]


def convert_to_list(node):
    result = []
    levelorder(node, lambda item: result.append(item))
    return result
