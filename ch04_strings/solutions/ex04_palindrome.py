# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch04_strings.solutions.ex03_reverse_string import reverse


def is_palindrome(input):
    left = 0
    right = len(input) - 1

    lower_input = input.lower()
    is_same_char = True
    while left < right and is_same_char:
        is_same_char = (lower_input[left] == lower_input[right])
        left += 1
        right -= 1

    return is_same_char


def is_palindrome_rec(input):
    return is_palindrome_rec_in_range(input.lower(), 0, len(input) - 1)


def is_palindrome_rec_in_range(input, left, right):
    if left >= right:
        return True

    if input[left] == input[right]:
        return is_palindrome_rec_in_range(input, left + 1, right - 1)

    return False


def is_palindrome_special(input, ignore_spaces_and_punctuation):
    adjusted_input = input.lower()
    if ignore_spaces_and_punctuation:
        adjusted_input = adjusted_input.replace(" ", "")
        adjusted_input = adjusted_input.replace("!", "")
        adjusted_input = adjusted_input.replace(".", "")

    return is_palindrome_rec(adjusted_input)


import re


def is_palindrome_special_with_reg_ex(input, ignore_spaces_and_punctuation):
    adjusted_input = input.lower()
    if ignore_spaces_and_punctuation:
        adjusted_input = re.sub(r"[ !\.\?]", "", adjusted_input)

    return is_palindrome_rec(adjusted_input)



def is_palindrome_with_reverse(input):
    adjusted_input = input.lower()

    return adjusted_input == reverse(adjusted_input)


def is_palindrome_short(input):
    adjusted_input = input.lower()

    return adjusted_input == adjusted_input[::-1]


def main():
    print(is_palindrome("ABBA"))
    print(is_palindrome("MICHA"))

    print(is_palindrome_short("ABBA"))
    print(is_palindrome_short("MICHA"))

    print(is_palindrome_rec("ABBA"))
    print(is_palindrome_rec("MICHA"))

    print(is_palindrome_special("Dreh mal am Herd.", True))
    print(is_palindrome_special("Dreh mal am Herd.", False))


if __name__ == "__main__":
    main()
