# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def all_palindrome_parts_rec(input):
    results = set()

    __all_palindrome_parts_rec(input, 0, len(input) - 1, results)

    return results


def __all_palindrome_parts_rec(input, left, right, results):
    if left >= right:
        return

    # Prüfe, ob der gesamte String ein Palindrom ist
    complete_is_palindrome = is_palindrome_rec(input, left, right)
    if complete_is_palindrome:
        new_candidate = input[left: right + 1]
        results.add(new_candidate)

    # 2) Alle von links testen
    for i in range(left + 1, right):
        left_part_is_palindrome = is_palindrome_rec(input, i, right)
        if left_part_is_palindrome:
            new_candidate = input[i: right + 1]
            results.add(new_candidate)

    # 3) Alle von rechtstesten
    for i in range(right - 1, left, -1):
        right_part_is_palindrome = is_palindrome_rec(input, left, i)
        if right_part_is_palindrome:
            new_candidate = input[left: i + 1]
            results.add(new_candidate)

    # rekursiver Abstieg
    __all_palindrome_parts_rec(input, left + 1, right - 1, results)


def longest_palindrome_part(input):
    all_palindrome_parts = all_palindrome_parts_rec(input)

    longest = ''
    for word in all_palindrome_parts:
        if len(word) > len(longest):
            longest = word

    return longest


def is_palindrome_rec(input, left, right):
    if left >= right:
        return True

    if input[left] == input[right]:
        return is_palindrome_rec(input, left + 1, right - 1)

    return False


def all_palindrome_parts_rec_optimized(input):
    results = set()

    __all_palindrome_parts_rec_optimized(input, 0, len(input) - 1, results)

    return results


def __all_palindrome_parts_rec_optimized(input, left, right, results):
    # rekursiver Abbruch
    if left >= right:
        return

    # 1) Prüfe, ob der gesamte String ein Palindrom ist
    if is_palindrome_rec(input, left, right):
        results.add(input[left: right + 1])

    # rekursiver Abstieg: 2) + 3) von links / rechts testen
    __all_palindrome_parts_rec_optimized(input, left + 1, right, results)
    __all_palindrome_parts_rec_optimized(input, left, right - 1, results)


def all_palindrome_parts_rec_optimized_v3(input):
    results = set()

    __all_palindrome_parts_rec_optimized_v3(input, results)

    return results


def __all_palindrome_parts_rec_optimized_v3(input, results):
    # rekursiver Abbruch
    if len(input) < 2:
        return

    # 1) Prüfe, ob der gesamte String ein Palindrom ist
    if is_palindrome_rec(input, 0, len(input) - 1):
        results.add(input)

    # rekursiver Abstieg: 2) + 3) von links / rechts testen
    __all_palindrome_parts_rec_optimized_v3(input[1:], results)
    __all_palindrome_parts_rec_optimized_v3(input[0:len(input) - 1], results)


def main():
    palindrome_and_longest("racecar")
    palindrome_and_longest("ABALOTTOLL")
    palindrome_and_longest("BCDEDCB")
    print(is_palindrome_rec("dreh_malam_herd", 0, len("drah_malam_herd")-1))
    palindrome_and_longest("dreh_malam_herd")


def palindrome_and_longest(input):
    print(all_palindrome_parts_rec(input))
    print(all_palindrome_parts_rec_optimized(input))
    print(all_palindrome_parts_rec_optimized_v3(input))
    print("longest: " + longest_palindrome_part(input))


if __name__ == "__main__":
    main()
