# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import itertools
import time


def calc_permutations(input):
    # rekursiver Abbruch
    if is_blank(input) or len(input) == 1:
        return {input}

    combinations = set()

    #  Extrahiere i-tes Zeichen als neues erstes Zeichen
    for i, new_first in enumerate(input):

        # rekursiver Abstieg für Rest ohne i-tes Zeichen
        permutations = calc_permutations(input[0:i] + input[i + 1:])

        # Hinzufügen des extrahierten Zeichens zu allen Teillösungen
        for perm in permutations:
            combinations.add(new_first + perm)

    return combinations


def is_blank(my_string):
    return not (my_string and my_string.strip())


def calc_permutations_mini_opt(input):
    return __calc_permutations_mini_opt_helper(input, "")


def __calc_permutations_mini_opt_helper(remaining, prefix):
    # rekursiver Abbruch
    if len(remaining) == 0:
        return {prefix}

    candidates = set()

    for i in range(len(remaining)):
        new_prefix = prefix + remaining[i]
        new_remaining = remaining[0: i] + remaining[i + 1:]

        candidates.update(__calc_permutations_mini_opt_helper(new_remaining,
                                                              new_prefix))

    return candidates



def calc_permutations_built_in(input):
    result_tuples = list(itertools.permutations(input))

    return {"".join(tuple) for tuple in result_tuples}


def calc_permutations_built_in_single_elements(input):
    return set(itertools.permutations(input))






def main():
    print(calc_permutations("AB"))
    print(calc_permutations("ABC"))
    print(calc_permutations("ABCD"))

    print(calc_permutations_mini_opt("AB"))
    print(calc_permutations_mini_opt("ABC"))
    print(calc_permutations_mini_opt("ABCD"))

    print(calc_permutations_built_in("AB"))
    print(calc_permutations_built_in("ABC"))
    print(calc_permutations_built_in("ABCD"))

    start = time.process_time()
    print(calc_permutations_built_in("abcdefghijk"))
    end = time.process_time()
    print("calc_permutations_built_in took %.2f ms" % ((end - start) * 1000))
    # 3455.54 ms


if __name__ == "__main__":
    main()
