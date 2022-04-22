# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch05_datastructures.util.queue import Queue
from ch08_binary_trees.solutions import ex13_print_tree
from ch08_binary_trees.util.binary_tree_node import BinaryTreeNode


def inorder(node, action):
    if node is None:
        return

    inorder(node.left, action)
    action(node.item)
    inorder(node.right, action)


def preorder(node, action):
    if node is None:
        return

    action(node.item)
    preorder(node.left, action)
    preorder(node.right, action)


def postorder(node, action):
    if node is None:
        return

    postorder(node.left, action)
    postorder(node.right, action)
    action(node.item)


def levelorder(start_node, action):
    if start_node is None:
        return

    to_process = Queue()
    to_process.enqueue(start_node)

    while not to_process.is_empty():
        current = to_process.dequeue()

        if current is not None:
            action(current.item)

            to_process.enqueue(current.left)
            to_process.enqueue(current.right)


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


def nice_print(node):
    ex13_print_tree.nice_print(node)


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
