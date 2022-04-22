# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import functools
import time

from functools import wraps


def fib_rec_orig(n):
    if n <= 0:
        raise ValueError("n must be >= 1")

    if n == 1 or n == 2:
        return 1

    # rekursiver Abstieg
    return fib_rec_orig(n - 1) + fib_rec_orig(n - 2)


def fib_rec(n):
    if n <= 0:
        raise ValueError("n must be >= 1")

    if n == 1 or n == 2:
        return 1

    # rekursiver Abstieg
    return fib_rec(n - 1) + fib_rec(n - 2)


# Hand gestrickt
def decorate_with_memo(func):
    lookup_map = dict()

    @wraps(func)
    def helper(n):
        # MEMOIZATION: prüfe, ob vorberechnetes Ergebnis existiert
        if n in lookup_map:
            return lookup_map[n]

        result = func(n)

        # MEMOIZATION: speichere berechnetes Ergebnis
        lookup_map[n] = result
        return result

    return helper


# Memoization nicht so klar
def decorate_with_memo_shorter_one_param(func):
    lookup_map = dict()

    @wraps(func)
    def helper(n):
        if n not in lookup_map:
            lookup_map[n] = func(n)

        return lookup_map[n]

    return helper


# Allgemeingültiger
def decorate_with_memo_shorter(func):
    lookup_map = dict()

    @functools.wraps(func)
    def helper(*args):
        if args not in lookup_map:
            lookup_map[args] = func(*args)

        return lookup_map[args]

    return helper



def check_argument_is_positive_integer(unary_func):
    def helper(n):
        if type(n) == int and n > 0:
            return unary_func(n)
        else:
            raise ValueError("n must be positive and of type int")

    return helper


# Annotiert
@check_argument_is_positive_integer
@decorate_with_memo_shorter
def fib_rec(n):
    if n == 1 or n == 2:
        return 1

    # rekursiver Abstieg
    return fib_rec(n - 1) + fib_rec(n - 2)



@check_argument_is_positive_integer
@functools.lru_cache(maxsize=None)
def fib_rec(n):
    if n == 1 or n == 2:
        return 1

    # rekursiver Abstieg
    return fib_rec(n - 1) + fib_rec(n - 2)




def main():

    print(fib_rec(50))


if __name__ == "__main__":
    main()
