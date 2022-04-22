# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


# noinspection Recursion should not be infinite
def infinite_recursion(value):  # NOSONAR
    infinite_recursion(value)


# noinspection python:S2190
def factorial_no_abortion(number):  # NOSONAR
    return number * factorial_no_abortion(number - 1)


def factorial_wrong_call(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    return n * factorial_wrong_call(n)


def main():
    infinite_recursion("INFINITE")
    # factorialNoAbortion(7)
    factorial_wrong_call(7)


if __name__ == "__main__":
    main()
