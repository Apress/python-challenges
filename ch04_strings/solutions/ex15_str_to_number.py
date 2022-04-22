# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def str_to_number_first_try(input):
    is_negative = input[0] == "-"
    value = 0

    startpos = 1 if starts_with_sign(input) else 0

    for pos in range(startpos, len(input)):
        digit_value = ord(input[pos]) - 48
        value = value * 10 + digit_value

    return -value if is_negative else value


def str_to_number(input):
    is_negative = input[0] == "-"
    value = 0

    startpos = 1 if starts_with_sign(input) else 0

    for pos in range(startpos, len(input)):
        if not input[pos].isdigit():
            raise ValueError(input + " contains not only digits")

        digit_value = ord(input[pos]) - 48
        value = value * 10 + digit_value

    return -value if is_negative else value


def str_to_number_bonus(input):
    is_negative = input[0] == "-"
    is_octal = input[0:2] == '0o' or \
               (starts_with_sign(input) and input[1:3] == "0o")

    value = 0
    factor = 8 if is_octal else 10

    startpos = calc_start_pos(input, is_octal)

    for pos in range(startpos, len(input)):
        if not input[pos].isdigit():
            raise ValueError(input + " contains not only digits")

        digit_value = ord(input[pos]) - 48
        if is_octal and digit_value >= 8:
            raise ValueError(input + " found digit >= 8")

        value = value * factor + digit_value

    return -value if is_negative else value


def calc_start_pos(input, is_octal):
    pos = 0
    if is_octal:
        pos = 3 if starts_with_sign(input) else 2
    elif starts_with_sign(input):
        pos = 1
    return pos


def starts_with_sign(input):
    return input[0] in ["-", "+"]


def starts_with_sign_old(input):
    return input[0] == "-" or input[0] == "+"


def main():
    octal_number = 0o7271
    print(octal_number)

    print(str_to_number_first_try("123"))
    print(str_to_number_first_try("+123"))
    print(str_to_number_first_try("-123"))


if __name__ == "__main__":
    main()
