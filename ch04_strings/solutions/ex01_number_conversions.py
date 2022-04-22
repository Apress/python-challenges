# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def is_binary_number(number):
    is_binary = True
    i = 0

    while i < len(number) and is_binary:
        current_char = number[i]
        is_binary = (current_char == "0" or current_char == "1")

        i += 1

    return is_binary


def is_binary_number_v2(number):
    i = 0
    while i < len(number) and number[i] in ["0", "1"]:
        i += 1

    return i >= len(number)


def is_binary_number_short_cut(number):
    for current_char in number:
        if current_char not in ["0", "1"]:
            return False
    return True


def is_binary_number_v3(number):
    try:
        int(number, 2)
        return True
    except ValueError:
        return False




def binary_to_decimal(number):
    if not is_binary_number(number):
        raise ValueError(number + " is not a binary number")

    decimal_value = 0
    for i, current_char in enumerate(number):
        value = int(current_char)
        decimal_value = decimal_value * 2 + value

    return decimal_value


def hex_to_decimal(number):
    if not is_hex_number(number):
        raise ValueError(number + " is not a hex number")

    decimal_value = 0
    for i, current_char in enumerate(number):

        if current_char.isdigit():
            value = int(current_char)
        else:
            value = ord(current_char.upper()) - ord("A") + 10

        decimal_value = decimal_value * 16 + value

    return decimal_value


def is_hex_number(number):
    for current_char in number:
        if current_char not in "0123456789ABCDEFabcdef":
            return False

    return True


def main():
    print(is_binary_number("1011"))
    print(is_binary_number("123"))

    print(binary_to_decimal("111"))

    print(is_hex_number("A1"))
    print(is_hex_number("72AF"))

    print(hex_to_decimal("A1"))
    print(hex_to_decimal("72AF"))

    print(hex_to_decimal("a1"))
    print(hex_to_decimal("72af"))


if __name__ == "__main__":
    main()
