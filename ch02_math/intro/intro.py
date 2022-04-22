# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def extract_digits(number):
    remaining_value = number
    while remaining_value > 0:
        digit = remaining_value % 10
        remaining_value = remaining_value // 10
        print(digit, end=' ')
    print()


def extract_digits(number):
    remaining_value = number
    while remaining_value > 0:
        remaining_value, digit = divmod(remaining_value, 10)
        print(digit, end=' ')
    print()


def count_digits(number):
    count = 0
    remaining_value = number
    while remaining_value > 0:
        remaining_value = remaining_value // 10
        count += 1
    return count


def find_proper_divisors_v1(value):
    divisors = []

    for i in range(1, int(value / 2) + 1):
        if value % i == 0:
            divisors.append(i)

    return divisors


def find_proper_divisors_v2(value):
    divisors = []

    for i in range(1, value // 2 + 1):
        if value % i == 0:
            divisors.append(i)

    return divisors


def find_proper_divisors(value):
    return [i for i in range(1, value // 2 + 1) if value % i == 0]


def is_prime(potentially_prime):
    for i in range(2, potentially_prime // 2 + 1):
        if potentially_prime % i == 0:
            return False

    return True


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 != 0


def main():
    extract_digits(123)

    print(count_digits(101))
    print(count_digits(10101))

    print(find_proper_divisors_v1(6))
    print(find_proper_divisors_v1(28))
    print(find_proper_divisors_v1(40))
    print(find_proper_divisors_v2(6))
    print(find_proper_divisors_v2(28))
    print(find_proper_divisors_v2(40))
    print(find_proper_divisors(6))
    print(find_proper_divisors(28))
    print(find_proper_divisors(40))

    print(is_prime(3))
    print(is_prime(5))
    print(is_prime(7))
    print(is_prime(10))

    primes = []
    for i in range(2, 25):
        if is_prime(i):
            primes.append(i)
    print("Primes < 25:", primes)


if __name__ == "__main__":
    main()
