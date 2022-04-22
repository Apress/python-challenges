# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


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


def find_min_shorter(values):
    return min(values)


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


def find_min_by_pos(values, start, end):
    min_pos = find_min_pos(values, start, end)
    return values[min_pos]


def find_max_by_pos(values, start, end):
    max_pos = find_max_pos(values, start, end)
    return values[max_pos]


def main():
    print(find_min([2, 3, 4, 5, 6, 7, 8, 9, 1, 10]))
    print(find_max([2, 3, 4, 5, 6, 7, 8, 9, 1, 10]))

    print(min([2, 3, 4, 5, 6, 7, 8, 9, 1, 10]))
    print(max([2, 3, 4, 5, 6, 7, 8, 9, 1, 10]))

    values_min = [5, 3, 4, 2, 6, 7, 8, 9, 1, 10]
    values_max = [1, 22, 3, 4, 5, 10, 7, 8, 9, 49]
    print("min pos all", find_min_pos(values_min, 0, len(values_min)))
    print("max pos all", find_max_pos(values_max, 0, len(values_min)))
    print("min pos 1-7", find_min_pos(values_min, 1, 7))
    print("max pos 1-7", find_max_pos(values_max, 1, 7))

    print(find_min_by_pos(values_min, 0, len(values_min)))
    print(find_max_by_pos(values_max, 0, len(values_min)))
    print(find_min_by_pos(values_min, 1, 7))
    print(find_max_by_pos(values_max, 1, 7))


if __name__ == "__main__":
    main()
