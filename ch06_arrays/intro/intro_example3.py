# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import numpy as np


def remove_duplicates_new_array(sorted_numbers):
    unique_values = set(sorted_numbers)

    return np.array(unique_values)


def remove_duplicates_new_array2(sorted_numbers):
    # Reihenfolge wechselt potenziell
    # unique_values = list(set(sorted_numbers))

    # Reihenfolge stabil
    unique_values = list(dict.fromkeys(sorted_numbers))

    return np.array(unique_values)


def remove_duplicates_stable(numbers):
    return np.array(collect_unique_values_stable(numbers))


def collect_unique_values_stable(numbers):
    result = []
    unique_values = set()
    for value in numbers:
        if not value in unique_values:
            unique_values.add(value)
            result.append(value)

    return result


def collect_unique_values_stable_shorter(numbers):
    return list(dict.fromkeys(numbers))


def remove_duplicates_inplace_first_try(sorted_numbers):
    prev_value = sorted_numbers[0]
    write_pos = 1
    read_pos = 1

    while read_pos < len(sorted_numbers):
        current_value = sorted_numbers[read_pos]
        if prev_value != current_value:
            sorted_numbers[write_pos] = current_value
            write_pos += 1

            prev_value = current_value

        read_pos += 1


def remove_duplicates_inplace_improved(sorted_numbers):
    write_index = 1

    for i in range(1, len(sorted_numbers)):
        current_value = sorted_numbers[i]
        prev_value = sorted_numbers[write_index - 1]

        if prev_value != current_value:
            sorted_numbers[write_index] = current_value
            write_index += 1

    # Löschen der nicht mehr benötigten Positionen
    for i in range(write_index, len(sorted_numbers)):
        sorted_numbers[i] = -1

    return write_index



def main():
    sorted_numbers = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    no_duplicates = remove_duplicates_new_array(sorted_numbers)
    print(no_duplicates)

    sorted_numbers = np.array([1, 2, 2, 3, 3, 4, 4, 5, 6, 7,8,9,9,10,11,12,13,13, 17, 21.5, 42.0])
    no_duplicates = remove_duplicates_new_array(sorted_numbers)
    print(no_duplicates)

    sorted_numbers2 = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    no_duplicates2 = remove_duplicates_new_array2(sorted_numbers2)
    print(no_duplicates2)

    sorted_numbers2 = np.array([1, 2, 2, 3, 3, 4, 4, 5, 6, 7,8,9,9,10,11,12,13,13, 17, 21.5, 42.0])
    no_duplicates2 = remove_duplicates_new_array2(sorted_numbers2)
    print(no_duplicates2)

    numbers = np.array([1, 4, 4, 2, 2, 3, 4, 3, 4])
    no_duplicates2 = remove_duplicates_stable(numbers)
    print("remove_duplicates_stable", no_duplicates2)


    sorted_numbers2 = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    remove_duplicates_inplace_first_try(sorted_numbers2)
    print(sorted_numbers2)

    sorted_numbers3 = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    remove_duplicates_inplace_improved(sorted_numbers3)
    print(sorted_numbers3)


if __name__ == "__main__":
    main()
