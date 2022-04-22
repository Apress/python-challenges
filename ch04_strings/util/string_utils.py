# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden



def check_no_duplicate_chars(input):
    upper_case_input = input.upper()
    return len(upper_case_input) == len(set(upper_case_input))


def is_palindrome_rec(input):
    return is_palindrome_rec_in_range(input.lower(), 0, len(input) - 1)


def is_palindrome_rec_in_range(input, left, right):
    if left >= right:
        return True

    if input[left] == input[right]:
        return is_palindrome_rec_in_range(input, left + 1, right - 1)

    return False


def is_anagram(str1, str2):
    char_counts1 = calc_char_frequencies(str1)
    char_counts2 = calc_char_frequencies(str2)

    return char_counts1 == char_counts2


def calc_char_frequencies(input):
    char_counts = {}

    for current_char in input.upper():
        if current_char in char_counts:
            char_counts[current_char] += 1
        else:
            char_counts[current_char] = 1

    return char_counts


def compare(val1, val2):
    if val1 < val2:
        return "<"
    if val1 > val2:
        return ">"
    return "="


def compare_versions(version1, version2):
    v1_numbers = version1.split(".")
    v2_numbers = version2.split(".")

    pos = 0
    compare_result = "="

    while (pos < len(v1_numbers) and
           pos < len(v2_numbers) and compare_result == "="):

        current_v1 = int(v1_numbers[pos])
        current_v2 = int(v2_numbers[pos])

        compare_result = compare(current_v1, current_v2)
        pos += 1

    #   Gleicher Beginn etwa 3.1 und 3.1.7
    if compare_result == "=":
       return compare(len(v1_numbers), len(v2_numbers))

    return compare_result
