# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch08_binary_trees.util import tree_utils
from ch08_binary_trees.intro.intro_binary_search_tree import insert
from ch08_binary_trees.intro.intro_binary_tree_node import BinaryTreeNode


def get_height(parent):
    # rekursiver Abbruch
    if parent is None:
        return 0

    # rekursiver Abstieg
    left_height = get_height(parent.left)
    right_height = get_height(parent.right)

    return 1 + max(left_height, right_height)


def main():
    e = BinaryTreeNode("E")
    insert(e, "C")
    insert(e, "A")
    insert(e, "G")
    insert(e, "F")
    insert(e, "H")
    insert(e, "I")

    tree_utils.nice_print(e)

    print_infos(e.left, e, e.right, e.right.right.right)


def print_infos(c, e, g, i):
    print("\nHeight of root E:", get_height(e))
    print("Height from left parent C: ", get_height(c))
    print("Height from right parent G:", get_height(g))
    print("Height from right child I: ", get_height(i))


if __name__ == "__main__":
    main()
