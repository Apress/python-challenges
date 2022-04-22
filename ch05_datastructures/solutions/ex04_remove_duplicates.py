# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def remove_duplicates(inputs):
    result = []

    already_found_numbers = set()

    for i, elem in enumerate(inputs):
        if elem not in already_found_numbers:
            already_found_numbers.add(elem)
            result.append(elem)

    return result


def remove_duplicates_with_dict(inputs):
    return list( dict.fromkeys(inputs))


def main():
    print(remove_duplicates([1, 1, 2, 3, 4, 1, 2, 3]))  # [1, 2, 3, 4]
    print(remove_duplicates([7, 5, 3, 5, 1]))  # [7, 5, 3, 1]
    print(remove_duplicates([1, 1, 1, 1]))  # [1]

    #######

    list_with_duplicates = ["a", "b", "a", "c", "d", "c", "d"]
    # Reihenfolge wechselt
    no_duplicates1 = list(set(list_with_duplicates))
    no_duplicates2 = remove_duplicates_with_dict(list_with_duplicates)
    print(no_duplicates1)
    print(no_duplicates2)


if __name__ == "__main__":
    main()



