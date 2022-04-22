# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 != 0


def is_prime(potentially_prime):
    for number in range(2, int(potentially_prime / 2) + 1):
        if potentially_prime % number == 0:
            return False

    return True


def count_digits(number):
    count = 0
    remaining_value = number
    while remaining_value > 0:
        remaining_value = remaining_value // 10
        count += 1
    return count


def is_perfect_number_based_on_proper_divisors(number):
    divisors = find_proper_divisors(number)

    return sum(divisors) == number


def find_proper_divisors(value):
    return [i for i in range(1, value // 2 + 1) if value % i == 0]


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


int_to_roman_digit_map = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
                          40: "XL", 50: "L", 90: "XC", 100: "C",
                          400: "CD", 500: "D", 900: "CM", 1000: "M"}
