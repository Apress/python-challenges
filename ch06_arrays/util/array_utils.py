# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import numpy as np


def swap(values, first, second):
    value1 = values[first]
    value2 = values[second]

    values[first] = value2
    values[second] = value1


def swap(values, first, second):
    tmp = values[first]

    values[first] = values[second]
    values[second] = tmp


def find(values, search_for):
    for i in range(len(values)):
        if values[i] == search_for:
            return i

    return -1


def find(values, search_for):
    pos = 0
    while pos < len(values) and not values[pos] == search_for:
        pos += 1

    # i >= len(values) or values[i] == searchFor
    return -1 if pos >= len(values) else pos


def find_with_enumerate(values, search_for):
    for i, value in enumerate(values):
        if value == search_for:
            return i

    return -1


def find_min(values):
    if len(values) == 0:
        raise ValueError("find_min not supported for empty input")

    min = values[0]
    for i in range(1, len(values)):
        if values[i] < min:
            min = values[i]

    return min


def find_max(values):
    if len(values) == 0:
        raise ValueError("find_max not supported for empty input")

    max = values[0]
    for i in range(1, len(values)):
        if values[i] > max:
            max = values[i]

    return max


def find_min_pos(values, start, end):
    if len(values) == 0:
        raise ValueError("find_min_pos not supported for empty input")
    if start < 0 or start > end or end > len(values):
        raise ValueError("invalid range")

    min_pos = start
    for i in range(start + 1, end):
        if values[i] < values[min_pos]:
            min_pos = i

    return min_pos


def find_max_pos(values, start, end):
    if len(values) == 0:
        raise ValueError("find_max_pos not supported for empty input")
    if start < 0 or start > end or end > len(values):
        raise ValueError("invalid range")

    max_pos = start
    for i in range(start + 1, end):
        if values[i] > values[max_pos]:
            max_pos = i

    return max_pos


def print_array(values2dim):
    max_y, max_x = get_dimension(values2dim)
    for y in range(max_y):
        for x in range(max_x):
            value = values2dim[y][x]
            print(str(value) + " ", end='')

        print()


def get_dimension(values2dim):
    if isinstance(values2dim, list):
        return (len(values2dim), len(values2dim[0]))

    if isinstance(values2dim, np.ndarray):
        return values2dim.shape

    raise ValueError("unsupported type", type(values2dim))


def swap_with_tuple(values, first, second):
    values[second], values[first] = values[first], values[second]


def main():
    numbers = np.array([1, 4, 3, 2, 5, 6])
    swap(numbers, 1, 3)
    print(numbers)

    if 2 in numbers:
        print("contains 2")

    print(find(numbers, 3))
    print(find(numbers, 7))

    numbers = np.array([3, 4, 1, 2, 5, 6])
    swap_with_tuple(numbers, 0, 2)
    swap_with_tuple(numbers, 1, 3)
    print(numbers)

    numbers = np.array([3, 4, 1, 2, 5, 6])
    print(find(numbers, 2))
    print(find_with_enumerate(numbers, 2))


if __name__ == "__main__":
    main()
