# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def swap_positions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]


def find_max_pos(values, start_pos, end_pos):
    max_pos = start_pos
    for i in range(start_pos + 1, end_pos):
        if values[i] > values[max_pos]:
            max_pos = i

    return max_pos


def selection_sort_max_inplace(values):
    for i in range(len(values) - 1, 0, -1):
        max_pos = find_max_pos(values, 0, i + 1)

        swap_positions(values, max_pos, i)


def selection_sort_max_copy(values):
    copy = list(values)
    selection_sort_max_inplace(copy)
    return copy


def main():
    values1 = [5, 2, 9, 1, 3, 7]
    values2 = [7, 2, 5, 1, 6, 8, 9, 4, 3]

    selection_sort_max_inplace(values1)
    print(values1)

    print(selection_sort_max_copy(values2))
    print(values2)


if __name__ == "__main__":
    main()
