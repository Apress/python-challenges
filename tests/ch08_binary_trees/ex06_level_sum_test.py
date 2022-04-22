# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

from ch08_binary_trees.solutions.ex06_levelsum import create_example_level_sum_tree, level_sum, level_sum_depth_first


def test_level_sum():
    root = create_example_level_sum_tree()

    result = level_sum(root)

    assert result == {0: 4, 1: 8, 2: 17, 3: 16}


def test_level_sum_depth_first():
    root = create_example_level_sum_tree()

    result = level_sum_depth_first(root)

    assert result == {0: 4, 1: 8, 2: 17, 3: 16}

