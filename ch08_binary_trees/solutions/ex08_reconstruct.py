# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch08_binary_trees.util import tree_utils
from ch08_binary_trees.intro.intro_binary_tree_node import BinaryTreeNode
from ch08_binary_trees.solutions.ex13_print_tree import nice_print


def reconstruct(values):
    if not values:
        return None

    mid_idx = len(values) // 2
    mid_value = values[mid_idx]

    new_node = BinaryTreeNode(mid_value)

    # rekursiver Abbruch
    if len(values) == 1:
        return new_node

    # rekursiver Abbstieg
    left_part = values[0: mid_idx]
    right_part = values[mid_idx + 1:len(values)]

    new_node.left = reconstruct(left_part)
    new_node.right = reconstruct(right_part)

    return new_node


def print_info(root):
    nice_print(root)

    print("Root: ", root.item)
    print("Left: ", root.left.item)
    print("Right:", root.right.item)
    print()


def reconstruct_clearer(preorder_values, inorder_values):
    # rekursiver Abbruch
    # len(values) == 0 not recommended by PEP 8
    if not preorder_values or not inorder_values:
        return None

    root_value = preorder_values[0]
    root = BinaryTreeNode(root_value)

    # rekursiver Abbruch
    if len(preorder_values) == 1 and len(inorder_values) == 1:
        return root

    # rekursiver Abstieg
    index = inorder_values.index(root_value)

    # linker und rechter Teil für Inorder
    left_inorder = inorder_values[0: index]
    right_inorder = inorder_values[index + 1: len(inorder_values)]

    # linker und rechter Teil für Preorder
    left_preorder = preorder_values[1: 1 + index]
    right_preorder = preorder_values[index + 1: len(preorder_values)]

    root.left = reconstruct_clearer(left_preorder, left_inorder)
    root.right = reconstruct_clearer(right_preorder, right_inorder)

    return root


def reconstruct_from_preorder_bst(preorder_values):
    # rekursiver Abbruch
    if not preorder_values:
        return None

    root_value = preorder_values[0]
    root = BinaryTreeNode(root_value)

    # Aufspaltung
    left_values = [value for value in preorder_values if value < root_value]
    right_values = [value for value in preorder_values if value > root_value]

    # rekursiver Abbstieg
    root.left = reconstruct_from_preorder_bst(left_values)
    root.right = reconstruct_from_preorder_bst(right_values)

    return root


def reconstruct_and_print(preorder_values, inoder_values):
    root = reconstruct_clearer(preorder_values, inoder_values)
    tree_utils.nice_print(root)

    print("Root: ", root.item)
    print("Left: ", root.left.item)
    print("Right:", root.right.item)
    print()


def main():
    inputs = [[1, 2, 3, 4, 5, 6, 7],
              [1, 2, 3, 4, 5, 6, 7, 8]]

    for values in inputs:
        root = reconstruct(values)
        print_info(root)

    print("£££££££££££££££££££££££££££££££££")

    pre_inorder_pairs = [([4, 2, 1, 3, 6, 5, 7], [1, 2, 3, 4, 5, 6, 7]),
                         ([5, 4, 2, 1, 3, 7, 6, 8], [1, 2, 3, 4, 5, 6, 7, 8])]

    for pre_inorder_pair in pre_inorder_pairs:
        preorder_values = pre_inorder_pair[0]
        inorder_values = pre_inorder_pair[1]

        reconstruct_and_print(preorder_values, inorder_values)

    print("£££££££££££££££££££££££££££££££££")

    inputs = [[4, 2, 1, 3, 6, 5, 7],
              [5, 4, 2, 1, 3, 7, 6, 8]]

    for values in inputs:
        root = reconstruct_from_preorder_bst(values)
        nice_print(root)


if __name__ == "__main__":
    main()
