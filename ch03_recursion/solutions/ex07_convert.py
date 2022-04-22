# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def to_binary(n):
    if n < 0:
        raise ValueError("n must be >= 0")

    # rekursiver Abbruch: prüfe auf Ziffer im Binärsystem
    if n <= 1:
        return str(n)

    last_digit = n % 2
    remainder = n // 2

    # rekursiver Abstieg
    return to_binary(remainder) + str(last_digit)


def to_octal(n):
    if n < 0:
        raise ValueError("n must be >= 0")

    # rekursiver Abbruch: prüfe auf Ziffer im Binärsystem
    if n <= 7:
        return str(n)

    remainder, last_digit = divmod(n, 8)

    # rekursiver Abstieg
    return to_octal(remainder) + str(last_digit)


def to_hex(n):
    if n < 0:
        raise ValueError("n must be >= 0")

    # rekursiver Abbruch: prüfe auf Ziffer im Hexadezimalsystem if (n <= 15)
    if n <= 15:
        return as_hex_digit(n)

    remainder, last_digit = divmod(n, 16)

    # rekursiver Abstieg
    return to_hex(remainder) + as_hex_digit(last_digit)


# einfachere Handhabung der Hexadezimalumwandlung
def as_hex_digit(n):
    if n < 0:
        raise ValueError("n must be >= 0")

    if n < 9:
        return str(n)
    if n <= 15:
        # spezielle Character-Arithmetik
        return chr(ord('A') + (n - 10))

    raise ValueError("value not in range 0 - 15, " + "but is: " + n)


def as_hex_digit_optimized(n):
    if n < 0:
        raise ValueError("n must be >= 0")

    if n <= 15:
        return "0123456789ABCDEF"[n]

    raise ValueError("value not in range 0 - 15, " + "but is: " + n)


def to_binary_short(n):
    return int(n, 2)


def to_octal_short(n):
    return int(n, 8)


def to_hex_short(n):
    return int(n, 16)


def main():
    print(to_binary(5))
    print(to_binary(7))
    print(to_binary(11))
    print(to_binary(21))

    print(to_octal(11))
    print(to_octal(21))

    print(to_hex(7))
    print(to_hex(11))
    print(to_hex(15))
    print(to_hex(255))

    print("-----------")
    print(to_binary(7))
    print(to_binary(11))
    print(to_octal(7))
    print(to_octal(11))
    print(to_octal(21))
    print(to_hex(7))
    print(to_hex(15))


if __name__ == "__main__":
    main()
