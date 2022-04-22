# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import time


def fib_rec(n):
    if n <= 0:
        raise ValueError("n must be >= 1")

    if n == 1 or n == 2:
        return 1

    # rekursiver Abstieg
    return fib_rec(n - 1) + fib_rec(n - 2)


def fibonacci_optimized(n):
    return fibonacci_memo(n, {})


def fibonacci_memo(n, lookup_map):
    if n <= 0:
        raise ValueError("n must be > 0")

    # MEMOIZATION: prüfe, ob vorberechnetes Ergebnis existiert
    if n in lookup_map:
        return lookup_map.get(n)

    # normaler Algorithmus mit Hilfsvariable für Resultat
    result = 0

    # rekursiver Abbruch
    if n == 1 or n == 2:
        result = 1
    # rekursiver Abstieg
    else:
        result = fibonacci_memo(n - 1, lookup_map) + fibonacci_memo(n - 2, lookup_map)

    # MEMOIZATION: speichere berechnetes Ergebnis
    lookup_map[n] = result

    return result


def main():
    # Dauert sehr lange
    start = time.process_time()
    print("fibRec(40)", fib_rec(40))
    end = time.process_time()
    print("fibRec(40) took %.2f ms" % ((end - start) * 1000))

    start = time.process_time()
    print("fibRec(47)", fib_rec(47))
    end = time.process_time()
    print("fibRec(47) took %.2f ms" % ((end - start) * 1000))

    ####

    start = time.process_time()
    print("fibonacciOptimized(40)", fibonacci_optimized(47))
    end = time.process_time()
    print("fibonacciOptimized(40) took %.2f ms" % ((end - start) * 1000))

    start = time.process_time()
    print("fibonacciOptimized(47)", fibonacci_optimized(47))
    end = time.process_time()
    print("fibonacciOptimized(47) took %.2f ms" % ((end - start) * 1000))

    start = time.process_time()
    print("fibonacciOptimized(721)", fibonacci_optimized(721))
    end = time.process_time()
    print("fibonacciOptimized(721) took %.2f ms" % ((end - start) * 1000))


if __name__ == "__main__":
    main()
