# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch05_datastructures.solutions.ex02_stack import Stack


def reverse(values):
    result = []

    for i in range(len(values) - 1, -1, -1):
        result.append(values[i])

    return result


def reverse_with_comprehension(values):
    return [values[i] for i in range(len(values) - 1, -1, -1)]


def reverse_with_comprehension_nicer(values):
    return [value for value in reversed(values)]


def reverse_with_slicing(values):
    return values[::-1]


def reverse_inplace(original):
    left = 0
    right = len(original) - 1

    #   laufe von links und rechts, tausche jeweils positionsbasiert die Elemente
    while left < right:
        left_elem = original[left]
        right_elem = original[right]

        #   swap
        original[left] = right_elem
        original[right] = left_elem

        left += 1
        right -= 1

    return original


def list_reverse_with_stack(inputs):
    # Idee: Durchlaufe die Liste von vorne nach hinten (performant) und // befülle einen Stack
    all_values = Stack()

    for element in inputs:
        all_values.push(element)

    # Entleere den Stack und befülle eine Ergebnisliste final List<T> result = new ArrayList<>();
    result = []
    while not all_values.is_empty():
        result.append(all_values.pop())

    return result


def main():
    print(reverse([1, 2, 3, 4, 5, 6]))
    print(reverse_with_comprehension([1, 2, 3, 4, 5, 6]))
    print(reverse_with_comprehension_nicer([1, 2, 3, 4, 5, 6]))
    print(reverse_with_slicing([1, 2, 3, 4, 5, 6]))

    print(reverse_inplace(["M", "i", "c"]))
    print(reverse_inplace(["T", "I", "M"]))

    print(list_reverse_with_stack(["M", "i", "c"]))
    print(list_reverse_with_stack(["T", "I", "M"]))


if __name__ == "__main__":
    main()
