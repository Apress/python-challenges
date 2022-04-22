# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import numpy as np

from ch02_math.solutions.ex01_basics import is_odd, is_even
from ch06_arrays.intro.intro import swap


def order_even_before_odd(numbers):
    i = 0
    while i < len(numbers):
        value = numbers[i]

        if is_even(value):
            # gerade Zahl, also weiter mit nächster Zahl
            i += 1
        else:
            # ungerade Zahl, springe über alle ungeraden, bis zur ersten geraden
            j = i + 1
            while j < len(numbers) and not is_even(numbers[j]):
                j += 1

            if j < len(numbers):
                swap(numbers, i, j)
            else:
                break  # keine weiteren Zahlen

            i += 1


def order_even_before_odd_optimized(numbers):
    next_even = 0
    next_odd = len(numbers) - 1

    while next_even < next_odd:
        current_value = numbers[next_even]
        if is_even(current_value):
            next_even += 1
        else:
            swap(numbers, next_even, next_odd)

            next_odd -= 1


def order_even_before_odd_optimized_v2(numbers):
    left = 0
    right = len(numbers) - 1

    while left < right:
        # laufe bis zur ersten ungeraden Zahl oder zum Array-Ende
        while left < len(numbers) and is_even(numbers[left]):
            left += 1

        # laufe bis zur ersten geraden Zahl oder zum Array-Anfang
        while right >= 0 and is_odd(numbers[right]):
            right -= 1

        if left < right:
            swap(numbers, left, right)
            left += 1
            right -= 1


def main():
    values = [1, 2, 3, 4, 5, 6, 7]
    order_even_before_odd(values)
    print(values)

    values2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    order_even_before_odd(values2)
    print(values2)

    values3 = [2, 4, 6, 1, 8]
    print(order_even_before_odd(values3))
    values4 = [2, 4, 6, 8, 1]
    print(order_even_before_odd(values4))
    print(order_even_before_odd([]))

    def myprint(item):
        print(item, end=' ')

    one_to_seven = [1, 2, 3, 4, 5, 6, 7]
    order_even_before_odd_optimized(one_to_seven)
    print(one_to_seven)
    print(order_even_before_odd_optimized([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    print(order_even_before_odd_optimized([2, 4, 6, 1, 8]))
    print(order_even_before_odd_optimized([2, 4, 6, 8, 1]))
    print(order_even_before_odd_optimized([]))

    values_one_to_seven = [1, 2, 3, 4, 5, 6, 7]
    order_even_before_odd_optimized_v2(values_one_to_seven)
    print(values_one_to_seven)
    print(order_even_before_odd_optimized_v2([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    print(order_even_before_odd_optimized_v2([2, 4, 6, 1, 8]))
    print(order_even_before_odd_optimized_v2([2, 4, 6, 8, 1]))
    print(order_even_before_odd_optimized_v2([]))

    print("-------------------------")
    values = np.array([1, 2, 3, 4, 5, 6, 7])
    order_even_before_odd(values)
    print(values)

    values = np.array([1, 2, 3, 4, 5, 6, 7])
    order_even_before_odd_optimized(values)
    print(values)

    values = np.array([1, 2, 3, 4, 5, 6, 7])
    order_even_before_odd_optimized_v2(values)
    print(values)


if __name__ == "__main__":
    main()
