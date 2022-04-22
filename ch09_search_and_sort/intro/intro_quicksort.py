# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def quick_sort(values):
    # rekursiver Abbruch
    if len(values) <= 1:
        return values

    # Aufsammeln kleiner gleich / größer als Pivot
    pivot = values[0]

    below_or_equals = [value for value in values[1:] if value <= pivot]
    aboves = [value for value in values[1:] if value > pivot]

    # rekursiver Abstieg
    sorted_lowers_part = quick_sort(below_or_equals)
    sorted_uppers_part = quick_sort(aboves)

    # Zusammenfügen
    return sorted_lowers_part + [pivot] + sorted_uppers_part


def main():
    values = [4, 2, 7, 9, 1, 6, 5, 8, 3]
    print(quick_sort(values))

    values2 = [1, 2, 6, 9, 4, 7, 8, 3]
    print(quick_sort(values2))


if __name__ == "__main__":
    main()
