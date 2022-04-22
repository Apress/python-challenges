# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def gcd(a, b):
    # rekursiver Abbruch
    if b == 0:
        return a

    # rekursiver Abstieg
    return gcd(b, a % b)


def gcd_iterative(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    # hier gilt b == 0
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    print(gcd(2, 14))
    print(gcd(42, 14))

    print(gcd_iterative(2, 14))
    print(gcd_iterative(42, 14))

    print(lcm(2, 14))
    print(lcm(42, 14))


if __name__ == "__main__":
    main()
