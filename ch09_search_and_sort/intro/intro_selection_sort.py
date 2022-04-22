# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def selection_sort_min(values):
    for i in range(len(values) - 1):
        min_idx = i

        # Finde Minimum
        for j in range(i + 1, len(values)):
            if values[j] < values[min_idx]:
                min_idx = j

        # Tausche aktuellen Wert mit Minimum
        tmp = values[min_idx]
        values[min_idx] = values[i]
        values[i] = tmp


def selection_sort_min_readable(values):
    for cur_idx in range(len(values) - 1):
        min_idx = find_min_pos(values, cur_idx, len(values))
        swap(values, min_idx, cur_idx)


def find_min_pos(values, start_pos, end_pos):
    min_pos = start_pos
    for i in range(start_pos + 1, end_pos):
        if values[i] < values[min_pos]:
            min_pos = i

    return min_pos


def swap(values, pos1, pos2):
    temp = values[pos1]
    values[pos1] = values[pos2]
    values[pos2] = temp
