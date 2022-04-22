# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def check_no_duplicate_chars(input):
    contained_chars = set()

    for current_char in input.upper():
        if current_char in contained_chars:
            return False

        contained_chars.add(current_char)

    return True


def check_no_duplicate_chars_v2(input):
    upper_case_input = input.upper()
    return len(upper_case_input) == len(set(upper_case_input))


def main():
    print(check_no_duplicate_chars("Otto"))
    print(check_no_duplicate_chars("Adrian"))
    print(check_no_duplicate_chars("Micha"))
    print(check_no_duplicate_chars("ABCDEFG"))

    print(check_no_duplicate_chars_v2("Otto"))
    print(check_no_duplicate_chars_v2("Adrian"))
    print(check_no_duplicate_chars_v2("Micha"))
    print(check_no_duplicate_chars_v2("ABCDEFG"))


if __name__ == "__main__":
    main()


