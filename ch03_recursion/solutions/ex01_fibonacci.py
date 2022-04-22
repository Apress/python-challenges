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


def main():
    print(fib_rec(5))
    print(fib_rec(10))

    print(fib_iterative(5))
    print(fib_iterative(10))

    #########################

    # RecursionError: maximum recursion depth exceeded in comparison
    # print(fibRec(1000))

    print(fib_rec(10))
    print(fib_iterative(1000))
    print(fib_iterative(10000))

    fib = lambda n: n if n < 2 else fib(n - 1) + fib(n - 2)
    print("fib(10)", fib(10))



if __name__ == "__main__":
    main()
