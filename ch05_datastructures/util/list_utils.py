# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

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


def main():
    pass


if __name__ == "__main__":
    main()
