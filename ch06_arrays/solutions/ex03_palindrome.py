# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def is_palindrome_rec(values):
    return is_palindrome_rec_in_range(values, 0, len(values) - 1)


def is_palindrome_rec_in_range(values, left, right):
    # rekursiver Abbruch
    if left >= right:
        return True

    # Prüfe links == rechts
    if values[left] == values[right]:
        # rekursiver Abstieg
        return is_palindrome_rec_in_range(values, left + 1, right - 1)

    return False


def is_palindrome_iterative(values):
    left = 0
    right = len(values) - 1

    same_value = True
    while left <= right and same_value:
        # Prüfe links == rechts und wiederhole, bis Unterschied auftritt
        same_value = values[left] == values[right]
        left += 1
        right -= 1

    return same_value


def is_palindrome_short(values):
    for i in range(len(values) // 2):
        if values[i] != values[len(values) - 1 - i]:
            return False

    return True


def is_palindrome_shorter(values):
    return values == values[::-1]


def main():
    print(is_palindrome_rec(["Ein", "Test", " – ", "Test", "Ein"]))
    print(is_palindrome_rec(["Max", "Mike", "Mike", "Max"]))
    print(is_palindrome_rec(["Tim", "Tom", "Mike", "Max"]))

    print(is_palindrome_iterative(["Ein", "Test", " – ", "Test", "Ein"]))
    print(is_palindrome_iterative(["Max", "Mike", "Mike", "Max"]))
    print(is_palindrome_iterative(["Tim", "Tom", "Mike", "Max"]))

    print(is_palindrome_short(["Ein", "Test", " – ", "Test", "Ein"]))
    print(is_palindrome_short(["Max", "Mike", "Mike", "Max"]))
    print(is_palindrome_short(["Tim", "Tom", "Mike", "Max"]))

    print(is_palindrome_shorter(["Ein", "Test", " – ", "Test", "Ein"]))
    print(is_palindrome_shorter(["Max", "Mike", "Mike", "Max"]))
    print(is_palindrome_shorter(["Tim", "Tom", "Mike", "Max"]))


if __name__ == "__main__":
    main()
