# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from enum import Enum
from random import randrange, randint


class Direction(Enum):
    N = (0, -1)
    NE = (1, -1)
    E = (1, 0)
    SE = (1, 1)
    S = (0, 1)
    SW = (-1, 1)
    W = (-1, 0)
    NW = (-1, -1)

    def to_dx_dy(self):
        return self.value

    @classmethod
    def provide_random_direction(cls):
        random_index = randrange(len(list(Direction)))
        return list(Direction)[random_index]


def main():
    print(Direction.provide_random_direction())
    print(Direction.provide_random_direction())
    print(Direction.provide_random_direction())

    dir = Direction.provide_random_direction()
    print(dir)
    print("dx:", dir.value[0])
    print("dy:", dir.value[1])
    print("dx:", dir.to_dx_dy()[0])
    print("dx:", dir.to_dx_dy()[1])

    würfel_augen = randint(1, 6)
    print(würfel_augen)


if __name__ == "__main__":
    main()
