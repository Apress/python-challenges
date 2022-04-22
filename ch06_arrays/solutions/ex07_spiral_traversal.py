# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from enum import Enum

from ch06_arrays.intro.intro import get_dimension


class Direction(Enum):
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)
    UP = (-1, 0)


def spiral_traversal(values2dim):
    pos_x = 0
    pos_y = 0

    min_x = 0
    min_y = 1
    max_y, max_x = get_dimension(values2dim)

    results = []

    dir = Direction.RIGHT
    steps = 0

    all_steps = max_y * max_x
    while steps < all_steps:
        # Aktion
        results.append(values2dim[pos_y][pos_x])

        if dir == Direction.RIGHT:
            if pos_x < max_x - 1:
                pos_x += 1
            else:
                dir = Direction.DOWN
                max_x -= 1

        if dir == Direction.DOWN:
            if pos_y < max_y - 1:
                pos_y += 1
            else:
                dir = Direction.LEFT
                max_y -= 1
        if dir == Direction.LEFT:
            if pos_x > min_x:
                pos_x -= 1
            else:
                dir = Direction.UP
                min_x += 1

        if dir == Direction.UP:
            if pos_y > min_y:
                pos_y -= 1
            else:
                dir = Direction.RIGHT
                min_y += 1

                pos_x += 1

        steps += 1

    return results


def main():
    numbers2 = [[1, 2, 3, 4, 5],
                [14, 15, 16, 17, 6],
                [13, 20, 19, 18, 7],
                [12, 11, 10, 9, 8]]

    print(spiral_traversal(numbers2))

    numbers = [[1, 2, 3, 4],
               [12, 13, 14, 5],
               [11, 16, 15, 6],
               [10, 9, 8, 7]]

    print(spiral_traversal(numbers))

    letter_pairs = [["AB", "BC", "CD", "DE"],
                   ["JK", "KL", "LM", "EF"],
                   ["IJ", "HI", "GH", "FG"]]

    print(spiral_traversal(letter_pairs))


if __name__ == "__main__":
    main()


