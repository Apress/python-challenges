# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch02_math.solutions.ex04_primes import calc_primes_up_to


def calc_prime_factors(value):
    all_primes = calc_primes_up_to(value)

    prime_factors = []
    remaining_value = value

    # solange gerade, immer wieder durch 2 teilen
    while remaining_value % 2 == 0 and remaining_value >= 2:
        remaining_value = remaining_value // 2
        prime_factors.append(2)

    # prüfe Rest auf Primzahl
    if is_prime(all_primes, remaining_value):
        prime_factors.append(remaining_value)
    else:
        # Rest ist keine Primzahl, weitere Prüfung
        while remaining_value > 1:
            for current_prime in all_primes:
                if remaining_value % current_prime == 0:
                    remaining_value = remaining_value // current_prime
                    prime_factors.append(current_prime)

                    # starte nochmal von vorne, weil jeder Teiler
                    # mehrfach vorkommen kann
                    break

    return prime_factors


def is_prime(all_primes, n):
    return n in all_primes


def calc_prime_factors_optimized(value):
    all_primes = calc_primes_up_to(value)

    prime_factors = []

    remaining_value = value
    while remaining_value > 1:
        for current_prime in all_primes:
            while remaining_value % current_prime == 0:
                remaining_value = remaining_value // current_prime
                prime_factors.append(current_prime)

    return prime_factors


def main():
    print(calc_prime_factors(28))
    print(calc_prime_factors(123))
    print(calc_prime_factors(7225))
    print(calc_prime_factors(7227))
    print("---------------")
    print(calc_prime_factors_optimized(28))
    print(calc_prime_factors_optimized(123))
    print(calc_prime_factors_optimized(7225))
    print(calc_prime_factors_optimized(7227))


if __name__ == "__main__":
    main()
