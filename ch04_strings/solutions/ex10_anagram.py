# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


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


def is_anagram_v2(str1, str2):
    char_counts1 = calc_char_frequencies_shorter(str1)
    char_counts2 = calc_char_frequencies_shorter(str2)

    return char_counts1 == char_counts2


def calc_char_frequencies_shorter(input):
    char_counts = {}

    for current_char in input.upper():
        char_counts[current_char] = char_counts.setdefault(current_char, 0) + 1

    return char_counts


def main():
    print(is_anagram("Otto", "Toto"))
    print(is_anagram("Mary", "Army"))
    print(is_anagram("Ananas", "Bananas"))
    print(is_anagram("Michael", "lamiche"))

    print(is_anagram_v2("Otto", "Toto"))
    print(is_anagram_v2("Mary", "Army"))
    print(is_anagram_v2("Ananas", "Bananas"))
    print(is_anagram_v2("Michael", "lamiche"))


if __name__ == "__main__":
    main()
