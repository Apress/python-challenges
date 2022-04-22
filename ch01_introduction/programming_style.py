# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

def reverse_string(input):
    # rekursiver Abbruch
    if len(input) <= 1:
        return input

    first_char = input[0]
    remaining = input[1:]

    # rekursiver Abstieg
    return reverse_string(remaining) + first_char


def reverse_string_short(input):
    return input if len(input) <= 1 else \
        reverse_string_short(input[1:]) + input[0]


def count_substrings(input, value_to_find):
    # rekursiver Abbruch
    if len(input) < len(value_to_find):
        return 0

    count = 0
    remaining = ""

    # startet der Text mit der Suchzeichenfolge?
    if input.startswith(value_to_find):
        # Treffer: Setze die Suche nach dem gefundenen
        # Begriff nach der Fundstelle fort
        remaining = input[len(value_to_find):]
        count = 1
    else:
        # entferne erstes Zeichen und suche erneut
        remaining = input[1:]

    # rekursiver Abstieg
    return count_substrings(remaining, value_to_find) + count


def count_substrings_short(input, value_to_find):
    return 0 if len(input) < len(value_to_find) else \
        (1 if input.startswith(value_to_find) else 0) + \
        count_substrings_short(input[1:], value_to_find)


def main():
    print(reverse_string("Michael"))
    print(reverse_string_short("Michael"))
    print(count_substrings("hahaho", "ha"))
    print(count_substrings("hahaho", "ho"))
    print(count_substrings("XXXX", "XX"))
    print(count_substrings_short("hahaho", "ho"))
    print(count_substrings_short("XXXX", "XX"))


if __name__ == "__main__":
    main()
