# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from functools import reduce


def factorial(n):
    if n <= 0:
        raise ValueError("n must be >= 1")

    # rekursiver Abbruch
    if n == 1:
        return 1

    # rekursiver Abstieg
    return n * factorial(n - 1)


def sum_rec(n):
    if n <= 0:
        raise ValueError("n must be >= 1")

    # rekursiver Abbruch
    if n == 1:
        return 1

    # rekursiver Abstieg
    return n + sum_rec(n - 1)


def is_palindrome_simple_recursive(values):
    # rekursiver Abbruch
    if len(values) <= 1:
        return True

    left = 0
    right = len(values) - 1

    if values[left] == values[right]:
        # Achtung: exklusive End
        remainder = values[left + 1: right]

        # rekursiver Abstieg
        return is_palindrome_simple_recursive(remainder)

    return False


def is_palindrome_recursive_optimized(values):
    return is_palindrome_recursive_in_range(values, 0, len(values) - 1)


def is_palindrome_recursive_in_range(values, left, right):
    # rekursiver Abbruch
    if left >= right:
        return True

    if values[left] == values[right]:
        # rekursiver Abstieg
        return is_palindrome_recursive_in_range(values, left + 1, right - 1)

    return False


def is_palindrome_iterative(values):
    left = 0
    right = len(values) - 1

    same_value = True
    while left < right and same_value:
        same_value = values[left] == values[right]
        left += 1
        right -= 1

    return same_value


def is_palindrome_iterative_compact(values):
    left = 0
    right = len(values) - 1

    while left < right and values[left] == values[right]:
        left += 1
        right -= 1

    # left >= right or values[left] != values[right]
    return left >= right


def is_palindrome_shorter(values):
    return values == values[::-1]


def fractal_generator(n):
    if n < 1:
        return

    if n == 1:
        print("-")
    else:
        fractal_generator(n - 1)
        print("=" * n)
        fractal_generator(n - 1)


def multiply_all_digits(value):
    remainder = value // 10
    digit_value = value % 10

    print("multiply_all_digits: %-10d | remainder: %d, digit: %d" %
          (value, remainder, digit_value))

    if remainder > 0:
        result = multiply_all_digits(remainder)
        print("-> %d * %d = %d" % (digit_value, result, digit_value * result))
        return digit_value * result
    else:
        print("-> " + str(value))
        return value


def multiply_all_digits_shorter(value):
    return reduce(lambda x, y: int(x) * int(y), str(value))


def main():
    for n in range(1, 10):
        print("factorial(", n, "):", factorial(n))

    for n in range(1, 10):
        print("sum(", n, "):", sum_rec(n))

    print("sum(990)", sum_rec(990))

    factorial_rec2 = lambda n: n if n == 1 else n * factorial_rec2(n - 1)
    sum_rec2 = lambda n: n if n == 1 else n + sum_rec2(n - 1)
    print("factorial(5)", factorial_rec2(5))
    print("sum(990)", sum_rec2(990))

    print(is_palindrome_simple_recursive([1, 2, 3, 2, 1]))
    print(is_palindrome_simple_recursive([1, 2, 3, 4, 2, 1]))
    print(is_palindrome_recursive_optimized([1, 2, 3, 2, 1]))
    print(is_palindrome_recursive_optimized([1, 2, 3, 4, 2, 1]))

    print(is_palindrome_iterative([1, 2, 3, 2, 1]))
    print(is_palindrome_iterative([1, 2, 3, 4, 2, 1]))

    print(is_palindrome_shorter([1, 2, 3, 2, 1]))
    print(is_palindrome_shorter([1, 2, 3, 4, 2, 1]))


    fractal_generator(3)
    fractal_generator(4)

    print(multiply_all_digits(1234))
    print(multiply_all_digits_shorter(1234))


if __name__ == "__main__":
    main()
