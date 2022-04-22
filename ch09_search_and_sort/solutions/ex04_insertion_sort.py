# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def swap_positions_normal(list, pos1, pos2):
    tmp = list[pos1]
    list[pos2] = list[pos1]
    list[pos1] = tmp


def insertion_sort(values):
    for i in range(1, len(values)):
        # Prüfe, ob aktuelles Element grösser als Vorgänger
        current_idx = i
        while current_idx > 0 and values[current_idx - 1] > values[current_idx]:
            swap_positions(values, current_idx - 1, current_idx)
            current_idx -= 1


def swap_positions(values, pos1, pos2):
    values[pos1], values[pos2] = values[pos2], values[pos1]


def main():
    values1 = [5, 2, 9, 1, 3, 7]
    values2 = [7, 2, 5, 1, 6, 8, 9, 4, 3]

    insertion_sort(values1)
    insertion_sort(values2)

    print(values1)
    print(values2)


if __name__ == "__main__":
    main()
