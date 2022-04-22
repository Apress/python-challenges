# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def swap_positions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]


def quick_sort_inplace(values):
    quick_sort_in_range(values, 0, len(values) - 1)


def quick_sort_in_range(values, left, right):
    # rekursiver Abbruch
    if left >= right:
        return

    partition_index = partition(values, left, right)

    # rekursiver Abstieg
    quick_sort_in_range(values, left, partition_index - 1)
    quick_sort_in_range(values, partition_index + 1, right)


def partition(values, left, right):
    pivot = values[left]

    left_index = left + 1
    right_index = right

    while left_index < right_index:
        # Bewege die Position left_index nach rechts, so lange Wert kleiner
        # gleich Pivot und linke Grenze kleiner als rechte Grenze
        while values[left_index] <= pivot and left_index < right_index:
            left_index += 1

        # Bewege die Position right_index nach links, so lange Wert größer als
        # Pivot und rechte Grenze größer oder gleich linke Grenze
        while pivot < values[right_index] and right_index >= left_index:
            right_index -= 1

        if left_index < right_index:
            swap_positions(values, left_index, right_index)

    # Spezialfall 2-elementige(s) Array/Liste mit falscher Sortierung, aber kein
    # Durchlauf (wg. left_index == right_index) sowie Normalfall ganz am Ende
    if values[right_index] < pivot:
        swap_positions(values, left, right_index)

    return right_index




def main():
    values1 = [5, 2, 7, 1, 4, 3, 6, 8]
    values2 = [5, 2, 7, 9, 6, 3, 1, 4, 8]
    values3 = [5, 2, 7, 9, 6, 3, 1, 4, 2, 3, 8]

    quick_sort_inplace(values1)
    quick_sort_inplace(values2)
    quick_sort_inplace(values3)

    print(values1)
    print(values2)
    print(values3)


if __name__ == "__main__":
    main()
