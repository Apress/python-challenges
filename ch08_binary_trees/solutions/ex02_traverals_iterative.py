# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from enum import Enum, auto

from ch05_datastructures.solutions.ex02_stack import Stack
from ch08_binary_trees.util import tree_utils
from ch08_binary_trees.intro import example_trees
from ch08_binary_trees.util.binary_tree_node import BinaryTreeNode


def inorder_iterative(start_node, action):
    if start_node is None:
        return

    nodes_to_process = Stack()
    current_node = start_node

    # so lange noch Knoten auf dem Stack oder der aktuelle Knoten nicht None
    while not nodes_to_process.is_empty() or current_node is not None:
        if current_node is not None:
            # Abstieg nach links
            nodes_to_process.push(current_node)
            current_node = current_node.left
        else:
            # kein linker Nachfolger, dann aktuellen Knoten verarbeiten
            current_node = nodes_to_process.pop()
            action(current_node.item)

            # mit rechtem Nachfolger weitermachen
            current_node = current_node.right


def preorder_iterative(start_node, action):
    if start_node is None:
        return

    nodes_to_process = Stack()
    nodes_to_process.push(start_node)

    while not nodes_to_process.is_empty():
        current_node = nodes_to_process.pop()

        if current_node is not None:
            action(current_node.item)

            # damit links zuerst verarbeitet wird, hier Reihenfolge umgedreht
            nodes_to_process.push(current_node.right)
            nodes_to_process.push(current_node.left)


def postorder_iterative(start_node, action):
    if start_node is None:
        return

    nodes_to_process = Stack()
    current_node = start_node
    last_node_visited = None

    while not nodes_to_process.is_empty() or current_node is not None:
        if current_node != None:
            # Abstieg nach links
            nodes_to_process.push(current_node)
            current_node = current_node.left
        else:
            peek_node = nodes_to_process.peek()
            # Abstieg nach rechts
            if peek_node.right is not None and \
                last_node_visited != peek_node.right:
                current_node = peek_node.right
            else:
                # Verarbeitung von Sub-Wurzel oder Leaf
                last_node_visited = nodes_to_process.pop()
                action(last_node_visited.item)


def inorder_iterative_v2(root):
    stack = Stack()
    stack.push(root)

    while not stack.is_empty():
        current_node = stack.pop()
        if not current_node is None:
            if current_node.is_leaf():
                print(current_node.item, end=" ")
            else:
                stack.push(current_node.right)
                stack.push(BinaryTreeNode(current_node.item))
                stack.push(current_node.left)

    print()


def main():
    def myprint(item):
        print(item, end=' ')

    root = example_trees.create_example_tree()
    tree_utils.nice_print(root)

    print("inorder iterative:")
    inorder_iterative(root, myprint)
    print("\npreorder iterative:")
    preorder_iterative(root, myprint)
    print("\npostorder iterative:")
    postorder_iterative(root, myprint)
    print()

    print("\ninorder iterative v2:")
    inorder_iterative_v2(root)

    class Order(Enum):
        PREORDER = auto()
        INORDER = auto()
        POSTORDER = auto()

    def traverse(root, order):
        stack = Stack()
        stack.push(root)

        while not stack.is_empty():
            current_node = stack.pop()
            if not current_node is None:
                if current_node.is_leaf():
                    print(current_node.item, end = " ")
                else:
                    if order == Order.POSTORDER:
                        stack.push(BinaryTreeNode(current_node.item))

                    stack.push(current_node.right)

                    if order == Order.INORDER:
                        stack.push(BinaryTreeNode(current_node.item))

                    stack.push(current_node.left)

                    if order == Order.PREORDER:
                        stack.push(BinaryTreeNode(current_node.item))

        print()

    traverse(root, Order.PREORDER)
    traverse(root, Order.INORDER)
    traverse(root, Order.POSTORDER)


if __name__ == "__main__":
    main()
