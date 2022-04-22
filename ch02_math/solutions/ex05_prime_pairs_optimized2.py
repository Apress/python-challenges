# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch02_math.solutions.ex04_primes import calc_primes_up_to


def calc_prime_pairs_improved(max_value):
    twin_pairs = calc_pairs(max_value, 2)
    cousin_pairs = calc_pairs(max_value, 4)
    sexy_pairs = calc_pairs(max_value, 6)

    print("Twins:", twin_pairs)
    print("Cousins:", cousin_pairs)
    print("Sexy:", sexy_pairs)


def calc_pairs(max_value, distance):
    primes = calc_primes_up_to(max_value + distance)

    return {number: number + distance for number in range(1, 50)
            if is_prime(primes, number) and is_prime(primes, number + distance)}


def is_prime(primes, n):
    return n in primes


def main():
    calc_prime_pairs_improved(50)


if __name__ == "__main__":
    main()
