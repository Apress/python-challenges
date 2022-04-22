# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch08_binary_trees.util import tree_utils
from ch08_binary_trees.intro.intro_binary_tree_node import BinaryTreeNode
from ch08_binary_trees.intro.intro_binary_search_tree import insert


def create_lca_example_tree():
    _6 = BinaryTreeNode(6)
    insert(_6, 7)
    insert(_6, 4)
    insert(_6, 5)
    insert(_6, 2)
    insert(_6, 1)
    insert(_6, 3)

    return _6


def find_lca(start_node, value1, value2):
    # rekursiver Abbruch
    if start_node is None:
        return None

    current_value = start_node.item

    # rekursiver Abstieg
    if value1 < current_value and value2 < current_value:
        return find_lca(start_node.left, value1, value2)

    if value1 > current_value and value2 > current_value:
        return find_lca(start_node.right, value1, value2)

    # Hier gilt value1 < currentValue && currentValue < value2 bzw.
    # value2 < currentValue &&  currentValue < value1
    return start_node


def main():
    root = create_lca_example_tree()
    print("LCA: ", find_lca(root, 1, 5).item)

    tree_utils.nice_print(root)


if __name__ == "__main__":
    main()
