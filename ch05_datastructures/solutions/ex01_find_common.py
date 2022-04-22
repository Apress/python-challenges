# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def find_common_build_in(values1, values2):
    return set(values1).intersection(values2)


def find_common_short(values1, values2):
    results = set()
    for elem1 in values1:
        if elem1 in values2:
            results.add(elem1)
    return results


def find_common_short_comprehension(values1, values2):
    return {elem1 for elem1 in values1 if elem1 in values2}


def find_common(values1, values2):
    results = {}

    populate_from_collection1(values1, results)
    mark_if_also_in_second(values2, results)

    return remove_all_just_in_first(results)


def populate_from_collection1(values1, results):
    for elem1 in values1:
        results[elem1] = 1


def mark_if_also_in_second(values2, results):
    for elem2 in values2:
        if elem2 in results:
            results[elem2] += 1


def remove_all_just_in_first_old(results):
    final_result = set()

    for key, value in results.items():
        if value >= 2:
            final_result.add(key)

    return final_result


def remove_all_just_in_first(results):
    return {key for key, value in results.items() if value >= 2}



def main():
    print(find_common_build_in([1, 2, 4, 7, 8], [2, 3, 7, 9]))  # [2, 7]))
    print(find_common([1, 2, 4, 7, 8], [2, 3, 7, 9]))  # [2, 7]))
    print(find_common_short([1, 2, 4, 7, 8], [2, 3, 7, 9]))  # [2, 7]))
    print(find_common_short_comprehension([1, 2, 4, 7, 8], [2, 3, 7, 9]))  # [2, 7]))


if __name__ == "__main__":
    main()
