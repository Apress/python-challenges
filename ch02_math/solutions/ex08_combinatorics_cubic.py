# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import math


def solve_cubic_simple():
    for a in range(1, 100):
        for b in range(1, 100):
            for c in range(1, 100):
                for d in range(1, 100):
                    if a * a + b * b == c * c + d * d:
                        print("a =", a, " / b =", b, " / c =", c, " / d =", d)


def solve_cubic():
    for a in range(1, 100):
        for b in range(1, 100):
            for c in range(1, 100):
                value = a * a + b * b - c * c
                if value > 0:
                    d = int(math.sqrt(value))
                    if d < 100 and a * a + b * b == c * c + d * d:
                        print("a =", a, " / b =", b, " / c =", c, " / d =", d)


def solve_cubic_shorter():
    return [(a,b,c,d) for a in range(1, 100) for b in range(1, 100)
                      for c in range(1, 100) for d in range(1, 100)
                      if a * a + b * b == c * c + d * d]


def main():
    solve_cubic_simple()
    solve_cubic()

    print(solve_cubic_shorter())


if __name__ == "__main__":
    main()
