# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.item)
    inorder(node.right)


def preorder(node):
    if node is None:
        return

    print(node.item)
    preorder(node.left)
    preorder(node.right)


def postorder(node):
    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.item)
