# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import itertools


def is_prime(potentially_prime):
    for number in range(2, int(potentially_prime / 2) + 1):
        if potentially_prime % number == 0:
            return False

    return True


def erase_multiples_of_current(values, number):
    for n in range(number + number, len(values), number):
        values[n] = False
        # print("Eliminating:", n)


def build_primes_list(is_potentially_prime):
    return [number for number in range(2, len(is_potentially_prime))
            if is_potentially_prime[number]]


def build_primes_list_old(is_potentially_prime):
    primes = []
    for number in range(2, len(is_potentially_prime)):
        if is_potentially_prime[number]:
            primes.append(number)

    return primes


def calc_primes_up_to(max_value):
    # initial alle Werte als potenzielle Primzahl markieren
    is_potentially_prime = [True for _ in range(1, max_value + 2)]

    # Durchlaufe alle Zahlen startend bei 2,
    # Optimierung nur bis zur Hälfte
    for number in range(2, int(max_value / 2) + 1):
        if is_potentially_prime[number]:
            erase_multiples_of_current(is_potentially_prime, number)

    return build_primes_list(is_potentially_prime)


def calc_primes_up_to_v2(max_value):
    # initial alle Werte als potenzielle Primzahl markieren
    is_potentially_prime = [True for _ in range(1, max_value + 2)]

    # Durchlaufe alle Zahlen startend bei 2,
    # Optimierung nur bis zur Hälfte
    for number in range(2, max_value // 2 + 1):
        if is_potentially_prime[number]:
            erase_multiples_of_current(is_potentially_prime, number)

    is_potentially_prime[0:2] = False, False

    return list(itertools.compress(range(len(is_potentially_prime)),
                                   is_potentially_prime))


def main():
    print(calc_primes_up_to(50))
    print(calc_primes_up_to_v2(50))


if __name__ == "__main__":
    main()
