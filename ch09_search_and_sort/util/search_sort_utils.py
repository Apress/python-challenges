# Beispielprogramm für das Buch "Python Challenge"
#
# Copyright 2020 by Michael Inden

def last_index_of(values, search_for):
    for pos in range(len(values) - 1, -1, -1):
        if values[pos] == search_for:
            return pos

    return -1


def contains_all(values, search_for):
    for current in search_for:
        if current not in values:
            return False

    return True


def binary_search(values, search_value):
    left = 0
    right = len(values) - 1

    while right >= left:

        mid_idx = (left + right) // 2

        if search_value == values[mid_idx]:
            return mid_idx

        if search_value < values[mid_idx]:
            right = mid_idx - 1
        else:
            left = mid_idx + 1

    return -1
