# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def contains_all(values, search_for):
    for current in search_for:
        if not current in values:
            return False

    return True


def contains_all_v2(values, search_for):
    return all(elem in values for elem in search_for)


def main():
    print(contains_all([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [7, 2]))
    print(contains_all([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 11]))

    print(contains_all_v2([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [7, 2]))
    print(contains_all_v2([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 11]))


if __name__ == "__main__":
    main()
