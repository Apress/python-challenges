# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch08_binary_trees.util import tree_utils
from ch08_binary_trees.intro import example_trees


# Rotation
def rotate_left(node):
    if node.right is None:
        raise ValueError("can't rotate left, no valid root")

    rc = node.right
    rlc = node.right.left

    rc.left = node
    node.right = rlc

    return rc


def rotate_right(node):
    if node.left is None:
        raise ValueError("can't rotate right, no valid root")

    lc = node.left
    lrc = node.left.right

    lc.right = node
    node.left = lrc

    return lc


def main():
    root = example_trees.create_example_tree()
    tree_utils.nice_print(root)

    print("\nRotate left")
    left_rotated_root = rotate_left(root)
    tree_utils.nice_print(left_rotated_root)

    print("\nRotate right")
    right_rotated_root = rotate_right(rotate_right(left_rotated_root))
    tree_utils.nice_print(right_rotated_root)


if __name__ == "__main__":
    main()

