# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def fib_rec(n):
    if n <= 0:
        raise ValueError("n must be >= 1")

    if n == 1 or n == 2:
        return 1

    # rekursiver Abstieg
    return fib_rec(n - 1) + fib_rec(n - 2)


def fib_iterative(n):
    if n <= 0:
        raise ValueError("n must be >= 1")

    if n == 1 or n == 2:
        return 1

    fib_n_2 = 1
    fib_n_1 = 1

    for _ in range(2, n):
        fib_n = fib_n_1 + fib_n_2
        # um eins "weiterschieben"
        fib_n_2 = fib_n_1
        fib_n_1 = fib_n

    return fib_n


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


def is_number_palindrome_rec(number):
    return __is_number_palindrome_rec_helper(number, 0, number)


def __is_number_palindrome_rec_helper(original_number, current_value,
                                      remaining_value):
    #   rekursiver Abbruch
    if current_value == original_number:
        return True

    #   rekursiver Abbruch
    if (remaining_value < 1):
        return False

    last_digit = remaining_value % 10
    new_current = current_value * 10 + last_digit
    new_remaining = remaining_value // 10

    return __is_number_palindrome_rec_helper(original_number, new_current,
                                             new_remaining)


