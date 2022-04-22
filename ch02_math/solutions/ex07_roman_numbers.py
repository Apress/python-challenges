# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def from_roman_number_v1(roman_number):
    value = 0
    last_digit_value = 0

    for i in range(len(roman_number) - 1, -1, -1):
        roman_digit = roman_number[i]
        digit_value = value_map[roman_digit]

        add_mode = digit_value >= last_digit_value
        if add_mode:
            value += digit_value
            last_digit_value = digit_value
        else:
            value -= digit_value

    return value


def from_roman_number(roman_number):
    value = 0
    last_digit_value = 0

    for roman_digit in reversed(roman_number):
        digit_value = value_map[roman_digit]

        add_mode = digit_value >= last_digit_value
        if add_mode:
            value += digit_value
            last_digit_value = digit_value
        else:
            value -= digit_value

    return value


value_map = {"I": 1, "V": 5, "X": 10, "L": 50,
             "C": 100, "D": 500, "M": 1000}


def to_roman_number_v1(value):
    result = ""
    remainder = value

    # absteigende Sortierung
    for i in sorted(int_to_roman_digit_map.keys(), reverse=True):
        if remainder > 0:
            multiplier = i
            roman_digit = int_to_roman_digit_map[i]

            times = remainder // multiplier
            remainder = remainder % multiplier
            result += roman_digit * times

    return result


def to_roman_number(value):
    result = ""
    remainder = value

    # absteigende Sortierung
    for i in sorted(int_to_roman_digit_map.keys(), reverse=True):
        if remainder > 0:
            multiplier = i
            roman_digit = int_to_roman_digit_map[i]

            times, remainder = divmod(remainder, multiplier)
            result += roman_digit * times

    return result

# intuitive Variante, dann aber nicht korrekte
# XXXIIII
# XXXXVIIII
int_to_roman_digit_map_v1 = {1: "I", 5: "V", 10: "X", 50: "L",
                             100: "C", 500: "D", 1000: "M"}

int_to_roman_digit_map = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
                          40: "XL", 50: "L", 90: "XC", 100: "C",
                          400: "CD", 500: "D", 900: "CM", 1000: "M"}


def main():
    print(from_roman_number("VII"))
    print(from_roman_number("XXII"))
    print(from_roman_number("XXIXV"))

    print(to_roman_number(7))
    print(to_roman_number(15))
    print(to_roman_number(34))
    print(to_roman_number(49))


if __name__ == "__main__":
    main()
