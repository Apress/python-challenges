# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def all_combinations_with_value(base_values, desired_value):
    all_combinations = find_all_combinations(base_values)

    return find_by_value(all_combinations, desired_value)


def find_by_value(all_combinations, desired_value):
    return {key for key, value in all_combinations.items()
            if value == desired_value}


def find_all_combinations(digits):
    return __all_combinations_helper(digits, 0)


def __all_combinations_helper(digits, pos):
    #   rekursiver Abbruch: letzte Ziffer
    #   Keine Berechnungen, nur Ziffer
    if pos == len(digits) - 1:
        last_digit = digits[len(digits) - 1]
        return {last_digit: last_digit}

    #   rekursiver Abstieg
    results = __all_combinations_helper(digits, pos + 1)

    #   Erstelle alle Kombinationen
    solutions = {}

    current_digit = digits[pos]
    left = str(current_digit)

    for expression, value in results.items():
        right = str(expression)

        solutions[left + "+" + right] = eval(left + "+" + right)
        solutions[left + "-" + right] = eval(left + "-" + right)
        solutions[left + right] = eval(left + right)

    return solutions


def main():
    # print(findAllCombinations([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    print(all_combinations_with_value([1, 2, 3], 24))
    print(all_combinations_with_value([1, 2, 3, 4, 5], 42))
    print(all_combinations_with_value([1, 2, 3, 4, 5, 6], 75))
    print(all_combinations_with_value([1, 2, 3, 4, 5, 6, 7, 8, 9], 100))



if __name__ == "__main__":
    main()
