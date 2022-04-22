# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


class BinaryTreeNode:

    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item

    def is_leaf(self):
        return self.left is None and self.right is None

    def __str__(self):
        return "BinaryTreeNode [item=%s, left=%s, right=%s]" % (self.item, self.left, self.right)


def main():
    bt = BinaryTreeNode(7271)
    print(bt)


if __name__ == "__main__":
    main()
