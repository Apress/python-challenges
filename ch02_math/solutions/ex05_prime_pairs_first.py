# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch02_math.solutions.ex04_primes import calc_primes_up_to


def main():
    def is_twin_pair(n):
        return is_prime(n) and is_prime(n + 2)

    def is_cousin_pair(n):
        return is_prime(n) and is_prime(n + 4)

    def is_sexy_pair(n):
        return is_prime(n) and is_prime(n + 6)

    twin_pairs = {}

    for i in range(1, 50):
        if is_twin_pair(i):
            twin_pairs.update({i: i + 2})

    # Comprehensions
    cousin_pairs = {i: i + 4 for i in range(1, 50) if is_cousin_pair(i)}
    sexy_pairs = {i : i + 6 for i in range(1, 50) if is_sexy_pair(i)}

    print("Twins:", twin_pairs)
    print("Cousins:", cousin_pairs)
    print("Sexy:", sexy_pairs)


def is_prime(n):
    primes = calc_primes_up_to(n + 1)
    return n in primes


if __name__ == "__main__":
    main()
