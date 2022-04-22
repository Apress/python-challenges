# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import functools

# handgestrickt
def decorate_with_memo(func):
    lookup_map = dict()

    @functools.wraps(func)
    def helper(n):
        # MEMOIZATION: prüfe, ob vorberechnetes Ergebnis existiert
        if n in lookup_map:
            return lookup_map[n]

        result = func(n)

        # MEMOIZATION: speichere berechnetes Ergebnis
        lookup_map[n] = result
        return result

    return helper


# Memoization nicht so klar ersichtlich
def decorate_with_memo_shorter_one_param(func):
    lookup_map = dict()

    @functools.wraps(func)
    def helper(n):
        if n not in lookup_map:
            lookup_map[n] = func(n)

        return lookup_map[n]

    return helper


def decorate_with_memo_shorter_orig(func):
    lookup_map = dict()

    @functools.wraps(func)
    def helper(*args):
        if args in lookup_map:
            return lookup_map[args]
        else:
            result = func(*args)
            lookup_map[args] = result
            return result

    return helper


def decorate_with_memo_shorter(func):
    lookup_map = dict()

    @functools.wraps(func)
    def helper(*args):
        if args not in lookup_map:
            lookup_map[args] = func(*args)

        return lookup_map[args]

    return helper
