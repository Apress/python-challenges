# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import sys


def find_longest_growing_sequence(values):
    longest_subsequence = []
    current_subsequence = []

    last_value = sys.maxsize

    for current_value in values:
        if current_value >= last_value:
            last_value = current_value
            current_subsequence.append(current_value)
        else:
            # Ende dieser Sequenz, starte neue Sequenz
            if len(current_subsequence) >= len(longest_subsequence):
                longest_subsequence = current_subsequence

            current_subsequence = []
            last_value = current_value
            current_subsequence.append(current_value)

    # wichtig, weil sonst die letzte Sequenz ggf. nicht betrachtet wird
    if len(current_subsequence) >= len(longest_subsequence):
        longest_subsequence = current_subsequence

    return longest_subsequence


def find_longest_growing_sequence_mini_opt(values):
    longest_subsequence = []
    current_subsequence = []

    last_value = sys.maxsize

    for current_value in values:
        if current_value < last_value:
            # Ende dieser Sequenz, starte neue Sequenz
            if len(current_subsequence) >= len(longest_subsequence):
                longest_subsequence = current_subsequence

            current_subsequence = []

        last_value = current_value
        current_subsequence.append(current_value)

    # wichtig, weil sonst die letzte Sequenz ggf. nicht betrachtet wird
    if len(current_subsequence) >= len(longest_subsequence):
        longest_subsequence = current_subsequence

    return longest_subsequence


def find_longest_growing_sequence_optimized(values):
    if len(values) == 0:
        return values

    longest = (0, 0)
    start_current = 0
    end_current = 0

    for end_current in range(1, len(values)):
        if values[end_current] < values[end_current - 1]:
            if end_current - start_current > len(longest):
                longest = (start_current, end_current)
            start_current = end_current

    if end_current - start_current > len(longest):
        longest = (start_current, end_current)

    return values[longest[0]: longest[1]]


def main():
    print(find_longest_growing_sequence([7, 2, 7, 1, 2, 5, 7, 1]))  # [1, 2, 5, 7]
    print(find_longest_growing_sequence([7, 2, 7, 1, 2, 3, 8, 1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]]
    print(find_longest_growing_sequence([1, 1, 2, 2, 2, 3, 3, 3, 3]))  # [1, 1, 2, 2, 2, 3, 3, 3, 3]
    print(find_longest_growing_sequence([]))  # []

    print(find_longest_growing_sequence_mini_opt([7, 2, 7, 1, 2, 5, 7, 1]))  # [1, 2, 5, 7]
    print(find_longest_growing_sequence_mini_opt([7, 2, 7, 1, 2, 3, 8, 1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]]
    print(find_longest_growing_sequence_mini_opt([1, 1, 2, 2, 2, 3, 3, 3, 3]))  # [1, 1, 2, 2, 2, 3, 3, 3, 3]
    print(find_longest_growing_sequence_mini_opt([]))  # []

    print(find_longest_growing_sequence_optimized([7, 2, 7, 1, 2, 5, 7, 1]))  # [1, 2, 5, 7]
    print(find_longest_growing_sequence_optimized([7, 2, 7, 1, 2, 3, 8, 1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]]
    print(find_longest_growing_sequence_optimized([1, 1, 2, 2, 2, 3, 3, 3, 3]))  # [1, 1, 2, 2, 2, 3, 3, 3, 3]
    print(find_longest_growing_sequence_optimized([]))  # []


if __name__ == "__main__":
    main()
