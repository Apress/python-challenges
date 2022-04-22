# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch08_binary_trees.util import tree_utils
from ch08_binary_trees.intro import example_trees
from ch08_binary_trees.intro.intro_binary_tree_node import BinaryTreeNode


def is_symmetric(node):
    if node is None:
        return True

    return check_if_nodes_are_symmetric(node.left, node.right)


def check_if_nodes_are_symmetric(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False

    # Beide Teilbäume hinabsteigen
    return check_if_nodes_are_symmetric(left.right, right.left) and \
           check_if_nodes_are_symmetric(left.left, right.right)


def is_symmetric_with_values(node, check_value):
    if node is None:
        return True

    return check_if_nodes_and_values_are_symmetric(node.left, node.right, check_value)


def check_if_nodes_and_values_are_symmetric(left, right, check_value):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False

    # Prüfe die Werte
    if check_value and not left.item == right.item:
        return False

    # Beide Teilbäume hinabsteigen
    return check_if_nodes_and_values_are_symmetric(left.right, right.left,
                                                   check_value) and \
           check_if_nodes_and_values_are_symmetric(left.left, right.right,
                                                   check_value)


def create_symmetric_number_tree():
    root = BinaryTreeNode("1")
    root.left = BinaryTreeNode("2")
    root.right = BinaryTreeNode("2")
    root.left.left = BinaryTreeNode("3")
    root.right.right = BinaryTreeNode("3")
    return root


def check_symmetry(node):
    print("symmetric:", is_symmetric(node))
    print("isSymmetricNoValue:", is_symmetric_with_values(node, False))
    print("isSymmetricValue:  ", is_symmetric_with_values(node, True))
    print()


def invert(root):
    if root is None:
        return None

    inverted_right = invert(root.right)
    inverted_left = invert(root.left)

    root.left = inverted_right
    root.right = inverted_left

    return root


def invert_clearer(root):
    if root is None:
        return None

    root.left, root.right = invert(root.right), invert(root.left)

    return root


def main():
    root = example_trees.create_number_tree()
    tree_utils.nice_print(root)
    print("symmetric:", is_symmetric(root))
    check_symmetry(root)

    root2 = create_symmetric_number_tree()
    tree_utils.nice_print(root2)
    print("symmetric:", is_symmetric(root2))
    check_symmetry(root)

    # Modifizierter Baum: Füge eine 4 hinzu
    root2.right.left = BinaryTreeNode("4")
    tree_utils.nice_print(root2)
    print("symmetric:", is_symmetric(root2))

    print("Inverting")
    root = example_trees.create_number_tree()
    newroot = invert(root)
    tree_utils.nice_print(newroot)

    newroot = invert_clearer(newroot)
    tree_utils.nice_print(newroot)


if __name__ == "__main__":
    main()
