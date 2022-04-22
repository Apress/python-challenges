# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from enum import Enum

from ch06_arrays.intro.intro import get_dimension


class Direction(Enum):
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    UP = (0, -1)

    def next(self):
        keys = list(Direction.__members__.keys())
        pos = keys.index(self.name)
        return list(Direction)[(pos + 1) % len(keys)]


def spiral_traversal_optimized(values2dim):
    pos_x = 0
    pos_y = 0

    min_x = 0
    min_y = 0
    max_y, max_x = get_dimension(values2dim)

    results = []

    dir = Direction.RIGHT
    steps = 0

    all_steps = max_y * max_x
    while steps < all_steps:
        # Aktion
        results.append(values2dim[pos_y][pos_x])

        dx, dy = dir.value
        if is_outside(pos_x + dx, pos_y + dy, min_x, max_x, min_y, max_y):
            if dir == Direction.RIGHT:
                min_y += 1
            if dir == Direction.DOWN:
                max_x -= 1
            if dir == Direction.LEFT:
                max_y -= 1
            if dir == Direction.UP:
                min_x += 1

            dir = dir.next()
            dx, dy = dir.value

        pos_x += dx
        pos_y += dy
        steps += 1

    return results


def is_outside(x, y, min_x, max_x, min_y, max_y):
    return x < min_x or x >= max_x or y < min_y or y >= max_y


def main():
    numbers2 = [[1, 2, 3, 4, 5],
                [14, 15, 16, 17, 6],
                [13, 20, 19, 18, 7],
                [12, 11, 10, 9, 8]]

    print(spiral_traversal_optimized(numbers2))

    numbers = [[1, 2, 3, 4],
               [12, 13, 14, 5],
               [11, 16, 15, 6],
               [10, 9, 8, 7]]

    print(spiral_traversal_optimized(numbers))

    letter_pairs = [["AB", "BC", "CD", "DE"],
                   ["JK", "KL", "LM", "EF"],
                   ["IJ", "HI", "GH", "FG"]]

    print(spiral_traversal_optimized(letter_pairs))


if __name__ == "__main__":
    main()


