# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch05_datastructures.util.queue import Queue
from ch08_binary_trees.util import tree_utils
from ch08_binary_trees.intro.intro_binary_tree_node import BinaryTreeNode
from ch08_binary_trees.intro.intro_binary_search_tree import insert


def level_sum(start_node):
    if start_node is None:
        return {}

    result = {}

    to_process = Queue()
    # sehr cool, Tupel (node, level)
    to_process.enqueue((start_node, 0))

    while not to_process.is_empty():
        current_node_and_level = to_process.dequeue()

        current_node = current_node_and_level[0]
        level = current_node_and_level[1]

        if level not in result:
            result[level] = 0

        result[level] += current_node.item

        if current_node.left is not None:
            to_process.enqueue((current_node.left, level + 1))

        if current_node.right is not None:
            to_process.enqueue((current_node.right, level + 1))

    return result


def level_sum_depth_first(root):
    results = {}

    traverse_depth_first(root, 0, results)

    return dict(sorted(results.items()))


def traverse_depth_first(current_node, level, results):
    if current_node:
        # PREORDER
        # results[level] = results.get(level, 0) + current_node.item
        traverse_depth_first(current_node.left, level + 1, results)

        # INORDER
        results[level] = results.get(level, 0) + current_node.item

        traverse_depth_first(current_node.right, level + 1, results)

        # POSTORDER
        # results[level] = results.get(level, 0) + current_node.item


def create_example_level_sum_tree():
    _4 = BinaryTreeNode(4)
    insert(_4, 2)
    insert(_4, 1)
    insert(_4, 3)
    insert(_4, 6)
    insert(_4, 5)
    insert(_4, 8)
    insert(_4, 7)
    insert(_4, 9)

    return _4


def main():
    root = create_example_level_sum_tree()

    result = level_sum(root)
    print("\nlevel_sum:", result)

    result = level_sum_depth_first(root)
    print("\nlevel_sum_depth_first:", result)

    tree_utils.nice_print(root)


if __name__ == "__main__":
    main()
