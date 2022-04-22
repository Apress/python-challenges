# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def count_digits(value):
    if value < 0:
        raise ValueError("value must be >= 0")

    # rekursiver Abbruch
    if value < 10:
        return 1

    # rekursiver Abstieg
    return count_digits(value // 10) + 1


def count_digits_shorter(value):
    return sum([1 for _ in str(value)])


def count_digits_tricky(value):
    return len(str(value))


def calc_sum_of_digits(value):
    if value < 0:
        raise ValueError("value must be >= 0")

    # rekursiver Abbruch
    if value < 10:
        return value

    remainder = value // 10
    last_digit = value % 10

    # rekursiver Abstieg
    return calc_sum_of_digits(remainder) + last_digit



def calc_sum_of_digits_divmod(value):
    if value < 0:
        raise ValueError("value must be >= 0")

    # rekursiver Abbruch
    if value < 10:
        return value

    remainder, last_digit = divmod(value, 10)

    # rekursiver Abstieg
    return calc_sum_of_digits(remainder) + last_digit


def calc_sum_of_digits_shorter(value):
    return sum([int(ch) for ch in str(value)])


def main():
    print(count_digits(72))
    print(count_digits(7271))

    print(count_digits(72))
    print(count_digits(7271))

    print(calc_sum_of_digits(72))
    print(calc_sum_of_digits(7271))
    print(calc_sum_of_digits(123456))

    print(calc_sum_of_digits_shorter(72))
    print(calc_sum_of_digits_shorter(7271))
    print(calc_sum_of_digits_shorter(123456))


if __name__ == "__main__":
    main()
