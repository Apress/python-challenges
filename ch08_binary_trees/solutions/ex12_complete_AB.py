# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch08_binary_trees.util import tree_utils
from ch08_binary_trees.intro import example_trees
from ch08_binary_trees.solutions.ex03_tree_height import get_height


def count_nodes(node):
    if node is None:
        return 0

    return 1 + count_nodes(node.left) + count_nodes(node.right)


def is_full(root):
    if root is None:
        return True

    return __is_full_helper(root.left, root.right)


def __is_full_helper(left_node, right_node):
    if left_node is None and right_node is None:
        return True

    if left_node is not None and right_node is not None:
        return is_full(left_node) and is_full(right_node)

    return False


def is_perfect(node):
    if node is None:
        return True

    height = get_height(node)

    return is_perfect_helper(node.left, node.right, height, 1)


def is_perfect_helper(left_node, right_node, height, current_level):
    if left_node is None or right_node is None:
        return False

    if left_node.is_leaf() and right_node.is_leaf():
        return on_same_height(left_node, right_node, height, current_level)

    return is_perfect_helper(left_node.left, left_node.right, height,
                             current_level + 1) and \
           is_perfect_helper(right_node.left, right_node.right, height,
                             current_level + 1)


def on_same_height(left_node, right_node, height, current_level):
    # Problem Höhe von dem Knoten ist 1, deswegen müssen wir
    # hier noch das aktuelle Level mitberücksichtigen
    return get_height(left_node) + current_level == height and \
           get_height(right_node) + current_level == height


def main():
    _4 = example_trees.create_number_tree()
    tree_utils.nice_print(_4)

    print("#nodes:", count_nodes(_4))
    print("is_full?:", is_full(_4))
    print("is_perfect?:", is_perfect(_4))
    print()

    # Lösche Knoten mit den Werten 1, 3
    _4.left.left = None
    _4.left.right = None
    tree_utils.nice_print(_4)

    print("#nodes:", count_nodes(_4))
    print("is_full?:", is_full(_4))
    print("is_perfect?:", is_perfect(_4))
    print()


if __name__ == "__main__":
    main()
