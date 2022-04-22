# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch05_datastructures.util.queue import Queue
from ch08_binary_trees.intro.intro_binary_tree_node import BinaryTreeNode


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


def levelorder_recursive(start_node, action):
    if start_node is None:
        return

    to_process = Queue()
    to_process.enqueue(start_node)

    leve_order_recursive_helper(to_process, action)


def leve_order_recursive_helper(to_process, action):
    if to_process.is_empty():
        return

    current = to_process.dequeue()
    if current is not None:
        action(current.item)

        to_process.enqueue(current.left)
        to_process.enqueue(current.right)

    leve_order_recursive_helper(to_process, action)


def create_level_order_example_tree():
    _1 = BinaryTreeNode("1")
    _2 = BinaryTreeNode("2")
    _3 = BinaryTreeNode("3")
    _4 = BinaryTreeNode("4")
    _5 = BinaryTreeNode("5")
    _6 = BinaryTreeNode("6")
    _7 = BinaryTreeNode("7")

    _1.left = _2
    _1.right = _3
    _2.left = _4
    _2.right = _5
    _3.left = _6
    _3.right = _7

    return _1


def main():
    root = create_level_order_example_tree()
    print("\nLevelorder: ")
    levelorder(root, lambda item: print(item, end=' '))

    print("\nleveOrderRecursive: ")
    levelorder_recursive(root, lambda item: print(item, end=' '))


if __name__ == "__main__":
    main()
