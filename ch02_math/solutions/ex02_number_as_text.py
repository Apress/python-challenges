# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


value_to_text_mapping = {
    0: "ZERO", 1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR",
    5: "FIVE", 6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE"
}


def digit_as_text(n):
    return value_to_text_mapping[n % 10]


def number_as_text(n):
    value = ""

    remaining_value = n
    while remaining_value > 0:
        remainder_as_text = digit_as_text(remaining_value % 10)
        remaining_value = int(remaining_value / 10)
        value = remainder_as_text + " " + value

    return value.strip()


def number_as_text(n):
    value = ""

    remaining_value = n
    while remaining_value > 0:
        remaining_value, remainder = divmod(remaining_value, 10)
        value = digit_as_text(remainder) + " " + value

    return value.strip()


def number_as_text_shorter(n):
    value = ""

    for ch in str(n):
        value += digit_as_text(int(ch)) + " "

    return value.strip()


def main():
    print(value_to_text_mapping)

    print(digit_as_text(7))
    print(digit_as_text(2))

    print(number_as_text(7271))

    print(number_as_text_shorter(7271))


if __name__ == "__main__":
    main()
