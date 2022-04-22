# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch08_binary_trees.util import tree_utils
from ch08_binary_trees.intro.intro_binary_tree_node import BinaryTreeNode


def find(start_node, search_for):
    # rekursiver Abbruch
    if start_node is None:
        return None

    # rekursiver Abstieg nach links oder rechts je nach Vergleich
    if start_node.item < search_for:
        return find(start_node.right, search_for)
    if start_node.item > search_for:
        return find(start_node.left, search_for)

    return start_node


def insert(current_node, value):
    # rekursiver Abbruch
    if current_node is None:
        return BinaryTreeNode(value)

    # rekursiver Abstieg nach links oder rechts je nach Vergleich
    if value < current_node.item:
        current_node.left = insert(current_node.left, value)
    else:
        current_node.right = insert(current_node.right, value)

    return current_node


def main():
    _3 = BinaryTreeNode(3)
    insert(_3, 1)
    insert(_3, 2)
    insert(_3, 4)
    tree_utils.nice_print(_3)
    print("tree contains 2? ", find(_3, 2))
    print("tree contains 13?", find(_3, 13))

    _4 = BinaryTreeNode(4)
    insert(_4, 3)
    insert(_4, 2)
    insert(_4, 1)
    tree_utils.nice_print(_4)

    bst = BinaryTreeNode(7)
    insert(bst, 2)
    insert(bst, 4)
    insert(bst, 1)
    insert(bst, 12)
    insert(bst, 14)
    insert(bst, 11)
    tree_utils.nice_print(bst)


if __name__ == "__main__":
    main()
