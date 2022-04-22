# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import functools


def sum_rec(values):
    return sum_helper(values, 0)


def sum_helper(values, pos):
    # rekursiver Abbruch
    if pos >= len(values):
        return 0

    # rekursiver Abstieg
    return values[pos] + sum_helper(values, pos + 1)


def sum_tail(values):
    return sum_tail_helper(values, len(values) - 1)


def sum_tail_helper(values, pos):
    if pos < 0:
        return 0

    # rekursiver Abstieg
    return sum_tail_helper(values, pos - 1) + values[pos]


def sum_lambda(values):
    return functools.reduce(lambda x, y: x + y, values)


def main():
    print(sum([1, 2, 3, 4, 5]))
    print(sum([7, 3, 8, 2, 1]))
    print(sum([7, 3, 8, 2, 1]))

    print(sum_rec([1, 2, 3, 4, 5]))
    print(sum_rec([7, 3, 8, 2, 1]))
    print(sum_rec([7, 3, 8, 2, 1]))

    print(sum_lambda([1, 2, 3, 4, 5]))
    print(sum_lambda([7, 3, 8, 2, 1]))
    print(sum_lambda([7, 3, 8, 2, 1]))


if __name__ == "__main__":
    main()
