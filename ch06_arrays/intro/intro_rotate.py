# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import numpy as np

def rotate_right(values):
    if len(values) < 2:
        return values

    end_pos = len(values) - 1
    temp = values[end_pos]

    for i in range(end_pos, 0, -1):
        values[i] = values[i - 1]

    values[0] = temp


def rotate_right_slicing(values):
    if len(values) < 2:
        return values

    end_pos = len(values) - 1
    temp = values[end_pos]

    remaining = values[0 : end_pos]
    return [temp] + remaining


# mit Listen geht es so
def rotate_right_slicing_np(values):
    if len(values) < 2:
        return values

    end_pos = len(values) - 1
    temp = values[end_pos]

    remaining = values[0 : end_pos]
    return [temp] + remaining


def rotate_left(values):
    if len(values) < 2:
        return values

    end_pos = len(values) - 1
    temp = values[0]

    for i in range(end_pos):
        values[i] = values[i + 1]

    values[end_pos] = temp


def rotate_right_by_n_simple(values, n):
    for i in range(n):
        rotate_right(values)


def rotate_right_by_n(values, n):
    adjusted_n = n % len(values)
    temp_buffer = fill_temp_with_last_n(values, adjusted_n)

    # Kopiere n Positionen nach rechts
    for i in range(len(values) - 1, adjusted_n - 1, -1):
        values[i] = values[i - adjusted_n]

    copy_temp_buffer_to_start(temp_buffer, values)

    return values


def fill_temp_with_last_n(values, n):
    temp_buffer = np.arange(n)

    for i in range (n):
        temp_buffer[i] = values[len(values) - n + i]

    return temp_buffer


def copy_temp_buffer_to_start(temp_buffer, values):
    for  i in range(len(temp_buffer)):
        values[i] = temp_buffer[i]


def main():
    numbers1 = [1, 2, 3, 4]
    rotate_right(numbers1)
    print(numbers1)

    numbers = np.array([1, 2, 3, 4])
    rotate_right(numbers)
    print(numbers)

    numbers = np.array([1, 2, 3, 4])
    rotated = rotate_right_slicing_np(numbers)
    print(rotated)

    rotated = rotate_right_slicing([1, 2, 3, 4])
    print(rotated)

    numbers = np.array([1, 2, 3, 4])
    rotate_left(numbers)
    print(numbers)

    # slicing for reverse
    numbers = np.array([1, 2, 3, 4])
    numbers = numbers[::-1]
    print(numbers)

    numbers = np.array([1, 2, 3, 4, 5, 6, 7])
    rotate_right_by_n(numbers, 3)
    print(numbers)


if __name__ == "__main__":
    main()
