# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch08_binary_trees.intro.intro_binary_tree_node import BinaryTreeNode


def evaluate(node):
    value = node.item

    # kein switch in Python
    if value == "+":
        return evaluate(node.left) + evaluate(node.right)
    if value == "-":
        return evaluate(node.left) - evaluate(node.right)
    if value == "*":
        return evaluate(node.left) * evaluate(node.right)
    if value == "/":
        return evaluate(node.left) / evaluate(node.right)
    else:
        return int(value)


def main():
    plus = BinaryTreeNode("+")
    _3 = BinaryTreeNode("3")
    mult = BinaryTreeNode("*")
    _7 = BinaryTreeNode("7")
    minus = BinaryTreeNode("-")
    _1 = BinaryTreeNode("1")

    plus.left = _3
    plus.right = mult
    mult.left = _7
    mult.right = minus
    minus.left = _7
    minus.right = _1

    print("+:", evaluate(plus))
    print("*:", evaluate(mult))
    print("-:", evaluate(minus))


if __name__ == "__main__":
    main()
