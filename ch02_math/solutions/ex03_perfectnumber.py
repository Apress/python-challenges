# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch02_math.intro.intro import find_proper_divisors


def is_perfect_number_simple(number):
    # immer durch 1 teilbar
    sum_of_multipliers = 1

    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            sum_of_multipliers += i

    return sum_of_multipliers == number


def calc_perfect_numbers(max_exclusive):
    results = []

    for i in range(2, max_exclusive):
        if is_perfect_number_simple(i):
            results.append(i)

    return results


def calc_perfect_numbers_comprehension(max_exclusive):
    return [i for i in range(2, max_exclusive)
            if is_perfect_number_simple(i)]


def is_perfect_number_based_on_proper_divisors(number):
    divisors = find_proper_divisors(number)

    return sum(divisors) == number


def main():
    print(is_perfect_number_simple(6))
    print(is_perfect_number_simple(7))
    print(is_perfect_number_simple(24))
    print(is_perfect_number_simple(25))
    print(is_perfect_number_simple(28))

    print(calc_perfect_numbers(50))
    print(calc_perfect_numbers_comprehension(50))


if __name__ == "__main__":
    main()
