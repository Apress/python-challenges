# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def calc_checksum(input):
    if not input.isdigit():
        raise ValueError("illegal chars: not only digits")

    crc = 0

    for i, current_char in enumerate(input):
        value = (int(current_char)) * (i + 1)
        crc += value

    return int(crc % 10)


def main():
    print(calc_checksum("123"))
    print(calc_checksum("11111"))
    print(calc_checksum("87654321"))


if __name__ == "__main__":
    main()
