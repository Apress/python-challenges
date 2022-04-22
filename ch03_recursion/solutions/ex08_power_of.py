# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def is_power_of_2(n):
    # rekursiver Abbruch
    if n < 2:
        return n == 1

    if n % 2 != 0:
        return False

    # rekursiver Abstieg
    return is_power_of_2(n // 2)


def is_power_of_2_short(n):
    return n == 1 or n > 0 and n % 2 == 0 and is_power_of_2_short(n // 2)


def power_of(value, exponent):
    if exponent < 0:
        raise ValueError("exponent must be >= 0")

    # rekursiver Abbruch
    if exponent == 0:
        return 1
    if exponent == 1:
        return value

    # rekursiver Abstieg
    return value * power_of(value, exponent - 1)


def power_of_optimized(value, exponent):
    if exponent < 0:
        raise ValueError("exponent must be >= 0")

    # rekursiver Abbruch
    if exponent == 0:
        return 1
    if exponent == 1:
        return value

    # rekursiver Abstieg
    result = power_of_optimized(value * value, exponent // 2)
    if exponent % 2 == 1:
        return value * result

    return result


def power_of_iterative(value, exponent):
    result = 1
    while exponent > 0:
        result *= value
        exponent -= 1

    return result


def main():
    print(is_power_of_2(10))
    print(is_power_of_2(11))
    print(is_power_of_2(16))

    print(is_power_of_2_short(10))
    print(is_power_of_2_short(11))
    print(is_power_of_2_short(16))

    print(power_of(4, 2))
    print(power_of(5, 3))
    print(power_of(2, 8))
    print(power_of(10, 3))

    print(power_of_optimized(4, 2))
    print(power_of_optimized(5, 3))
    print(power_of_optimized(2, 8))
    print(power_of_optimized(10, 3))

    print(power_of_iterative(4, 2))
    print(power_of_iterative(5, 3))
    print(power_of_iterative(2, 8))
    print(power_of_iterative(10, 3))


if __name__ == "__main__":
    main()
