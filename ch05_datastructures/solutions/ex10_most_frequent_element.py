# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from operator import itemgetter


def value_count_old(values):

    value_to_count = {}

    for elem in values:
        if elem in value_to_count:
            value_to_count[elem] += 1
        else:
            value_to_count[elem] = 1

    return value_to_count


def value_count(values):

    value_to_count = {}

    for elem in values:
        if elem not in value_to_count:
            value_to_count[elem] = 0

        value_to_count[elem] += 1

    return value_to_count


def sort_dict_by_value(dictionary):
    return dict(sorted(dictionary.items(), key=itemgetter(1), reverse=True))


def main():
    print(value_count([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))

    result = value_count([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    reverse_sorted = sort_dict_by_value(result)
    print(reverse_sorted)

    result = value_count([1, 2, 2, 3, 3, 3])
    reverse_sorted = sort_dict_by_value(result)
    print(reverse_sorted)


if __name__ == "__main__":
    main()


