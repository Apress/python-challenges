# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch08_binary_trees.util import tree_utils
from ch08_binary_trees.intro.intro_binary_tree_node import BinaryTreeNode
from ch08_binary_trees.solutions.ex03_tree_height import get_height
from ch08_binary_trees.solutions.ex07_rotation import rotate_left, rotate_right

from ch08_binary_trees.intro import example_trees


def nice_print_v1(node):
    if node is None:
        return

    tree_height = get_height(node)
    all_nodes = fill_nodes_into_list(node)

    # laufe Level für Level
    offset = 0
    lines = []
    for level in range(tree_height):

        line_length = subtree_width(tree_height - 1 - level)

        # adjust previous lines
        for i in range(len(lines)):
            lines[i] = "   " + spacing(line_length) + lines[i]

        nodes_per_level = pow(2, level)
        node_line = ""
        connection_line = ""

        for pos in range(nodes_per_level):
            current_node = all_nodes[offset + pos]

            node_line += draw_node(current_node, line_length)
            node_line += spacing_between_nodes(tree_height, level)
            connection_line += draw_connections(current_node, line_length)
            connection_line += spacing_between_connections(tree_height, level)

        lines.append(node_line)
        lines.append(connection_line)

        # Springe im array weiter
        offset += nodes_per_level

    for line in lines:
        print(line)


def spacing_between_nodes(tree_height, level):
    spacing_length = subtree_width(tree_height - level)
    spacing = " " * spacing_length
    if spacing_length > 0:
        spacing += "   "
    return spacing


def spacing_between_connections(tree_height, level):
    spacing_length = subtree_width(tree_height - level)
    return " " * spacing_length


def draw_node(current_node, line_length):
    str_node = "   "
    str_node += spacing(line_length)
    str_node += stringify_node_value(current_node)
    str_node += spacing(line_length)

    return str_node


def stringify_node_value(node):
    if node is None:
        return "   "
    if node.item is None:
        return "   "

    node_value = str(node.item)
    if len(node_value) == 1:
        return " " + node_value + " "
    if len(node_value) == 2:
        return node_value + " "

    return node_value[0:3]


def spacing(line_length):
    return " " * line_length


def draw_connections(node, line_length):
    if node is None:
        return "   " + spacing(line_length) + \
               "   " + spacing(line_length) + "   "

    connection = draw_left_connection_part(node, line_length)
    connection += draw_junction(node)
    connection += draw_right_connection_part(node, line_length)

    return connection


def draw_left_connection_part(node, line_length):
    if node.left is None:
        return "   " + spacing(line_length)
    else:
        return " |-" + draw_line(line_length)


def draw_right_connection_part(node, line_length):
    if node.right is None:
        return spacing(line_length) + "   "
    else:
        return draw_line(line_length) + "-| "


def draw_junction(node):
    if node.left is None and node.right is None:
        return "   "
    elif node.left is None:
        return " +-"
    elif node.right is None:
        return "-+ "
    else:
        return "-+-"


def draw_line(line_length):
    return "-" * line_length


def subtree_width(height):
    if height <= 0:
        return 0

    leaf_width = 3
    spacing = 3

    max_num_of_leaves = pow(2, height - 1)
    width_of_tree = max_num_of_leaves * leaf_width + \
                    (max_num_of_leaves - 1) * spacing
    width_of_subtree = (width_of_tree - spacing) // 2

    return width_of_subtree


def fill_nodes_into_list(start_node):
    height = get_height(start_node)
    nodes = [None] * pow(2, height)

    traverse_and_mark(start_node, nodes, 0)

    return nodes


def traverse_and_mark(start_node, nodes, pos):
    if start_node is None:
        return

    if pos >= len(nodes):
        return

    # Aktion
    nodes[pos] = start_node

    # rekursiver Abstieg
    traverse_and_mark(start_node.left, nodes, pos * 2 + 1)
    traverse_and_mark(start_node.right, nodes, pos * 2 + 2)


def main():
    print(subtree_width(1))
    print(subtree_width(2))
    print(subtree_width(3))
    print(subtree_width(4))
    print("-----------------------")

    F = create_tree_print_example_tree()
    nice_print_v1(F)

    root = example_trees.create_example_tree()
    nice_print_v1(root)
    nice_print_v1(rotate_left(root))
    root = example_trees.create_example_tree()
    rotated_r = rotate_right(root)
    print("rotateRight(root)")
    nice_print_v1(rotated_r)

    print("rotateRight(rotated_r)")
    nice_print_v1(rotate_right(rotated_r))

    root = example_trees.create_example_tree()
    rotated_rr = rotate_right(rotate_right(root))
    nice_print_v1(rotated_rr)

    print("--------------------------------------")
    d4 = example_trees.create_example_tree()
    nice_print_v1(d4)

    BIG = create_big_tree()
    nice_print_v1(BIG)

    mon = create_monster_tree()
    nice_print_v1(mon)

    kk = create_kingkong()
    nice_print_v1(kk)


def create_big_tree():
    d4a = example_trees.create_example_tree()
    d4b = example_trees.create_example_tree()
    BIG = BinaryTreeNode("BIG")
    BIG.left = rotate_right(d4a)
    BIG.right = rotate_left(d4b)
    return BIG


def create_monster_tree():
    mon = BinaryTreeNode("MON")
    mon.left = create_big_tree()
    mon.right = create_big_tree()
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
