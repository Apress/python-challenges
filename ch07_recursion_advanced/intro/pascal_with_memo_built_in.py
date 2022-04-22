# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import functools
import time


def decorate_with_memo_shorter(func):
    lookup_map = dict()

    @functools.wraps(func)
    def helper(*args):
        if args not in lookup_map:
            lookup_map[args] = func(*args)

        return lookup_map[args]

    return helper


@decorate_with_memo_shorter
def pascal_rec(row, col):
    # rekursiver Abbruch: Spitze
    if col == 1 and row == 1:
        return 1

    # rekursiver Abbruch: Ränder
    if col == 1 or col == row:
        return 1

    # rekursiver Abstieg
    return pascal_rec(row - 1, col) + pascal_rec(row - 1, col - 1)


@functools.lru_cache(maxsize=None)
def pascal_rec2(row, col):
    # rekursiver Abbruch: Spitze
    if col == 1 and row == 1:
        return 1

    # rekursiver Abbruch: Ränder
    if col == 1 or col == row:
        return 1

    # rekursiver Abstieg
    return pascal_rec2(row - 1, col) + pascal_rec2(row - 1, col - 1)


def main():
    start = time.process_time()
    print("pascalRec(30, 15)", pascal_rec(30, 15))
    end = time.process_time()
    print("pascalRec(30, 15) took %.2f ms" % ((end - start) * 1000))

    start = time.process_time()
    print("pascalRec(30, 15)", pascal_rec2(30, 15))
    end = time.process_time()
    print("pascalRec(30, 15) took %.2f ms" % ((end - start) * 1000))


if __name__ == "__main__":
    main()
