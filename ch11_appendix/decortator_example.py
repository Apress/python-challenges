# Beispielprogramm für das Buch "Python Challenge"
#
# Copyright 2020 by Michael Inden


def check_argument_is_positive_integer(unary_func):
    def helper(n):
        if type(n) == int and n > 0:
            return unary_func(n)
        else:
            raise ValueError("n must be positive and of type int")

    return helper


def factorial(n):
    if n <= 0:
        raise ValueError("n must be >= 1")

    if n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))

# Wrapping in neue Funktion
checked_factorial = check_argument_is_positive_integer(factorial)
print(checked_factorial(5))
# print(checked_factorial(-5))

# Aufruf mit "factorial" als Parameter
print(check_argument_is_positive_integer(factorial)(5))
print(check_argument_is_positive_integer(factorial)(-5))
