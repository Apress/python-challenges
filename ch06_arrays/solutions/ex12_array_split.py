# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch06_arrays.intro.intro import swap


def array_split(values, reference_element):
    lesser = []
    bigger_or_equal = []

    for current in values:
        if current < reference_element:
            lesser.append(current)
        else:
            bigger_or_equal.append(current)

    return lesser + [reference_element] + bigger_or_equal


def array_split_nicer(values, reference_element):
    lesser = [value for value in values
              if value < reference_element]

    bigger_or_equal = [value for value in values
                       if value >= reference_element]

    return lesser + [reference_element] + bigger_or_equal


def array_split_inplace(values, reference_element):
    low = 0
    high = len(values) - 1

    while low < high:
        while low < high and values[low] < reference_element:
            low += 1

        while high > low and values[high] >= reference_element:
            high -= 1

        if low < high:
            swap(values, low, high)

    return values[:high] + [reference_element] + values[high + 1:]


def array_split_qs(values):
    reference_value = values[0]

    lesser = [values[i] for i in range(1, len(values))
              if values[i] < reference_value]

    bigger_or_equal = [values[i] for i in range(1, len(values))
                       if values[i] >= reference_value]

    return lesser + [reference_value] + bigger_or_equal


def array_split_qs_inplace(values):
    reference_value = values[0]

    low = 1
    high = len(values) - 1

    while low < high:
        while values[low] < reference_value and low < high:
            low += 1
        while values[high] >= reference_value and high >= low:
            high -= 1

        if low < high:
            swap(values, low, high)

    # wichtig für 1, 2 = > dann wäre 1 Pivot, nicht tauschen!
    if reference_value > values[high]:
        swap(values, 0, high)

    return values


def main():
    print(array_split([4, 7, 1, 20], 9))
    print(array_split([3, 5, 2], 7))
    print(array_split([2, 14, 10, 1, 11, 12, 3, 4], 7))
    print(array_split([3, 5, 7, 1, 11, 13, 17, 19], 11))

    print(array_split_nicer([4, 7, 1, 20], 9))
    print(array_split_nicer([3, 5, 2], 7))
    print(array_split_nicer([2, 14, 10, 1, 11, 12, 3, 4], 7))
    print(array_split_nicer([3, 5, 7, 1, 11, 13, 17, 19], 11))

    print(array_split_qs([9, 4, 7, 1, 20]))
    print(array_split_qs([7, 3, 5, 2]))
    print(array_split_qs([7, 2, 14, 10, 1, 11, 12, 3, 4]))
    print(array_split_qs([11, 3, 5, 7, 1, 11, 13, 17, 19]))

    print(array_split_qs_inplace([9, 4, 7, 1, 20]))
    print(array_split_qs_inplace([7, 3, 5, 2]))
    print(array_split_qs_inplace([7, 2, 14, 10, 1, 11, 12, 3, 4]))
    print(array_split_qs_inplace([11, 3, 5, 7, 1, 11, 11, 13, 17, 19]))


if __name__ == "__main__":
    main()
