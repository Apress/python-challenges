# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch09_search_and_sort.intro.intro_insertion_sort import insertion_sort


def merge_sort(to_sort):
    # Rekursiver Abbruch: Länge 0 (nur wenn initial leeres Array) oder 1
    if len(to_sort) <= 1:
        return to_sort

    # Rekursiver Abstieg: teile in zwei Hälften
    mid_pos = len(to_sort) // 2
    left = to_sort[0: mid_pos]
    result_left = merge_sort(left)

    right = to_sort[mid_pos: len(to_sort)]
    result_right = merge_sort(right)

    # Verbinde die Teilresultate zu größerer sortierter Liste
    return merge(result_left, result_right)


def merge_sort_with_insertion_sort(to_sort):
    # Rekursiver Abbruch inklusive Mini-Optimierung
    if len(to_sort) < 5:
        insertion_sort(to_sort)
        return to_sort

    # Rekursiver Abstieg: teile in zwei Hälften
    mid_pos = len(to_sort) // 2
    left = to_sort[0: mid_pos]
    result_left = merge_sort(left)

    right = to_sort[mid_pos: len(to_sort)]
    result_right = merge_sort(right)

    # Verbinde die Teilresultate zu größerer sortierter Liste
    return merge(result_left, result_right)


def merge(first, second):
    length1 = len(first)
    length2 = len(second)

    result = [0] * (length1 + length2)

    pos1 = 0
    pos2 = 0
    idx = 0

    # Durchlaufe solange die beiden Positionszeiger
    # unter der Länge sind
    while pos1 < length1 and pos2 < length2:

        value1 = first[pos1]
        value2 = second[pos2]

        if value1 < value2:
            result[idx] = value1
            idx += 1
            pos1 += 1
        else:
            result[idx] = value2
            idx += 1
            pos2 += 1

    # collect the remaining if any
    while pos1 < length1:
        result[idx] = first[pos1]
        idx += 1
        pos1 += 1

    while pos2 < length2:
        result[idx] = second[pos2]
        idx += 1
        pos2 += 1

    return result


def main():
    unsorted_values = [7, 2, 6, 3, 4, 5, 8, 1, 9]

    sorted_values = merge_sort(unsorted_values)
    print(sorted_values)

    unsorted_values2 = [7, 4, 2, 3, 2, 3, 1, 3, 4, 4, 8, 4, 9]

    sorted_values2 = merge_sort(unsorted_values2)
    print(sorted_values2)


if __name__ == "__main__":
    main()
