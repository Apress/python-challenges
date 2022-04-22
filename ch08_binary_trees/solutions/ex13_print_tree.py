# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch05_datastructures.util.queue import Queue
from ch08_binary_trees.util import tree_utils
from ch08_binary_trees.solutions.ex13_print_tree_V1 import subtree_width, spacing, draw_node, spacing_between_nodes, draw_connections, spacing_between_connections
from ch08_binary_trees.intro.intro_binary_tree_node import BinaryTreeNode
from ch08_binary_trees.solutions.ex03_tree_height import get_height
from ch08_binary_trees.solutions.ex07_rotation import rotate_left, rotate_right

from ch08_binary_trees.intro import example_trees



def nice_print(start_node):
    if start_node is None:
        return

    to_process = Queue()
    # sehr cool: Tupel (node, level)
    to_process.enqueue((start_node, 0))

    tree_height = get_height(start_node)
    lines = []

    level = 0
    node_line = ""
    connection_line = ""
    additional_left_spacing = ""

    while not to_process.is_empty() and level < tree_height:
        # Levelorder
        current_node_and_level = to_process.dequeue()
        current_node = current_node_and_level[0]
        node_level = current_node_and_level[1]

        line_length = subtree_width(tree_height - 1 - level)

        # Wechsel im der Ebene
        if level != node_level:
            level = node_level
            line_length = subtree_width(tree_height - 1 - level)

            lines.append(node_line)
            lines.append(connection_line)

            for i in range(len(lines)):
                lines[i] = "   " + additional_left_spacing + \
                           spacing(line_length) + lines[i]

            node_line = ""
            connection_line = ""

        node_line += draw_node(current_node, line_length)
        node_line += spacing_between_nodes(tree_height, level)
        connection_line += draw_connections(current_node, line_length)
        connection_line += spacing_between_connections(tree_height, level)

        # Levelorder
        if current_node is not None:
            to_process.enqueue((current_node.left, level + 1))
            to_process.enqueue((current_node.right, level + 1))
        else:
            # künstliche Platzhalter
            to_process.enqueue((None, level + 1))
            to_process.enqueue((None, level + 1))

    for line in lines:
        print(line)



def main():

    F = create_tree_print_example_tree()
    nice_print(F)

    root = example_trees.create_example_tree()
    nice_print(root)
    nice_print(rotate_left(root))
    root = example_trees.create_example_tree()
    rotated_r = rotate_right(root)
    print("rotateRight(root)")
    nice_print(rotated_r)
    nice_print(rotate_right(rotated_r))

    root = example_trees.create_example_tree()
    rotated_rr = rotate_right(rotate_right(root))
    nice_print(rotated_rr)

    print("--------------------------------------")
    root = example_trees.create_example_tree()
    nice_print(root)
    nice_print(rotate_left(root))
    nice_print(rotate_right(root))

    print("--------------------------------------")

    BIG = create_big_tree()
    nice_print(BIG)

    mon = create_monster_tree()
    nice_print(mon)

    kk = create_kingkong()
    nice_print(kk)


def create_big_tree():
    d4a = example_trees.create_example_tree()
    d4b = example_trees.create_example_tree()
    BIG = BinaryTreeNode("BIG")
    BIG.left = rotate_right(d4a)
    BIG.right = rotate_left(d4b)
    return BIG


def create_monster_tree():
    d4 = example_trees.create_example_tree()
    mon = BinaryTreeNode("MON")
    BIG = BinaryTreeNode("BIG")
    BIG.left = rotate_right(rotate_right(d4))
    BIG.right = rotate_left(d4)
    mon.left = BIG
    mon.right = BIG
    return mon

def create_kingkong():
    d4 = example_trees.create_example_tree()
    mon = BinaryTreeNode("KINGKONG")
    mon.left = create_monster_tree()
    mon.right = create_monster_tree()
    return mon

def create_tree_print_example_tree():
    F = BinaryTreeNode("F")
    tree_utils.insert(F, "D")
    tree_utils.insert(F, "H")
    tree_utils.insert(F, "B")
    tree_utils.insert(F, "A")
    tree_utils.insert(F, "C")
    tree_utils.insert(F, "I")
    return F


if __name__ == "__main__":
    main()
