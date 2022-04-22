# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch08_binary_trees.util import tree_utils
from ch08_binary_trees.intro.example_trees import create_integer_number_tree
from ch08_binary_trees.intro.intro_binary_tree_node import BinaryTreeNode


def is_bst(node):
    # rekursiver Abbruch
    if node is None:
        return True

    if node.is_leaf():
        return True

    # rekursiver Abstieg
    is_left_bst = True
    is_right_bst = True
    if node.left is not None:
        is_left_bst = node.left.item < node.item and is_bst(node.left)
    if node.right is not None:
        is_right_bst = node.right.item > node.item and is_bst(node.right)

    return is_left_bst and is_right_bst


def main():
    _4 = create_integer_number_tree()

    _2 = _4.left
    _6 = _4.right
    tree_utils.nice_print(_4)
    print("is_bst(_4):", is_bst(_4))
    print("is_bst(_2):", is_bst(_2))
    print("is_bst(_6):", is_bst(_6))

    # change tree on left side in a bad way, change right correctly
    _2.left = BinaryTreeNode(13)
    _6.right = None

    tree_utils.nice_print(_4)
    print("is_bst(_4):", is_bst(_4))
    print("is_bst(_2):", is_bst(_2))
    print("is_bst(_6):", is_bst(_6))


if __name__ == "__main__":
    main()
