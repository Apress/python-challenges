# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch08_binary_trees.util import tree_utils
from ch08_binary_trees.solutions.ex12_complete_AB import count_nodes
from ch08_binary_trees.intro.intro_binary_tree_node import BinaryTreeNode


def is_complete(start_node):
    node_count = count_nodes(start_node)

    node_exists = [False] * node_count

    #   jetzt durchlaufen wir den Baum von der Wurzel nach unten
    traverse_and_mark(start_node, node_exists, 0)

    return all_assigned(node_exists)


def traverse_and_mark(start_node, node_exists, pos):
    #   rekursiver Abbruch
    if start_node is None:
        return

    if pos >= len(node_exists):
        return

    #   Aktion
    node_exists[pos] = True

    #   rekursiver Abstieg
    traverse_and_mark(start_node.left, node_exists, pos * 2 + 1)
    traverse_and_mark(start_node.right, node_exists, pos * 2 + 2)


def all_assigned(node_exists):
    for exists in node_exists:
        if not exists:
            return False

    return True


def is_complete_rec(start_node):
    return __is_complete_rec_helper(start_node, 0, count_nodes(start_node))


def __is_complete_rec_helper(start_node, pos, node_count):
    if start_node is None:
        return True
    if pos >= node_count:
        return False

    if not __is_complete_rec_helper(start_node.left, 2 * pos + 1, node_count):
        return False

    if not __is_complete_rec_helper(start_node.right, 2 * pos + 2, node_count):
        return False

    return True


def main():
    F = create_completness_example_tree()
    tree_utils.nice_print(F)
    print("is_complete?", is_complete(F))
    print("is_complete_rec?", is_complete_rec(F))

    #   Modifikation: entferne Blätter unter H
    #F.right.left = None
    F.right.right = None
    tree_utils.nice_print(F)
    print("is_complete?", is_complete(F))
    print("is_complete_rec?", is_complete_rec(F))

    #   Modifikation: entferne Blätter unter H
    F.right.left = None
    tree_utils.nice_print(F)
    print("is_complete?", is_complete(F))
    print("is_complete_rec?", is_complete_rec(F))


def create_completness_example_tree():
    F = BinaryTreeNode("F")
    tree_utils.insert(F, "D")
    tree_utils.insert(F, "H")
    tree_utils.insert(F, "B")
    tree_utils.insert(F, "E")
    tree_utils.insert(F, "A")
    tree_utils.insert(F, "C")
    tree_utils.insert(F, "G")
    tree_utils.insert(F, "I")
    return F


if __name__ == "__main__":
    main()
