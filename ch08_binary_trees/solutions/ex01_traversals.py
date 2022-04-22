# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch08_binary_trees.util import tree_utils
from ch08_binary_trees.intro import example_trees


def inorder(node, action):
    if node is None:
        return

    inorder(node.left, action)
    action(node.item)
    inorder(node.right, action)


def myprint(item):
    print(item)


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


def to_list(start_node):
    if start_node is None:
        return []

    result = []

    result += to_list(start_node.left)
    result.append(start_node.item)
    result += to_list(start_node.right)

    return result


def to_list_preorder(start_node):
    if start_node is None:
        return []

    result = []

    result.append(start_node.item)
    result += to_list_preorder(start_node.left)
    result += to_list_preorder(start_node.right)

    return result


def to_list_postorder(start_node):
    if start_node is None:
        return []

    result = []

    result += to_list_postorder(start_node.left)
    result += to_list_postorder(start_node.right)
    result.append(start_node.item)

    return result

def main():
    def myprint(item):
        print(item, end=' ')

    root = example_trees.create_example_tree()
    tree_utils.nice_print(root)

    print("\ninorder with action:")
    inorder(root, myprint)
    print("\npreorder with action:")
    preorder(root, myprint)
    print("\npostorder with action:")
    postorder(root, myprint)

    print("\nto_list:", to_list(root))
    print("to_list_preorder:", to_list_preorder(root))
    print("to_list_postorder:", to_list_postorder(root))


if __name__ == "__main__":
    main()


