# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

import math


def solve_quadratic_simple():
    for a in range(1, 100):
        for b in range(1, 100):
            for c in range(1, 100):
                # if a ** 2 + b ** 2 == c ** 2:
                if a * a + b * b == c * c:
                    print("a =", a, "/ b =", b, "/ c =", c)


def solve_quadratic():
    for a in range(1, 100):
        for b in range(1, 100):
            c = int(math.sqrt(a * a + b * b))
            if c < 100 and a * a + b * b == c * c:
                print("a =", a, "/ b =", b, "/ c =", c)


def solve_quadratic_shorter():
    return [(a, b, c) for a in range(1, 100) for b in range(1, 100)
            for c in range(1, 100) if a * a + b * b == c * c]


def main():
    solve_quadratic_simple()
    solve_quadratic()

    print(solve_quadratic_shorter())


if __name__ == "__main__":
    main()
