# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def calc_pow_of_ten(number):
    return count_digits(number) - 1


# Funktioniert nur korrekt, wenn die Zahl keine Nullen enthält
def count_digits(number):
    count = 0

    while number > 0:
        number = number // 10
        count += 1

    return count


def is_number_palindrome(number):
    if number < 10:
        return True

    # geht nur, wenn es eine Ziffer >= 1 ist
    factor = calc_pow_of_ten(number)
    divisor = int(pow(10, factor))

    if number < divisor * 10:
        left_number = number // divisor
        right_number = number % 10
        # schneidet eine führende Null weg ...
        remaining_number = (number // 10) % (divisor // 10)

        return left_number == right_number and \
               is_number_palindrome(remaining_number)

    return False


def is_number_palindrome_rec(number):
    return __is_number_palindrome_rec_helper(number, 0, number)


def __is_number_palindrome_rec_helper(original_number, current_value,
                                      remaining_value):
    #   rekursiver Abbruch
    if current_value == original_number:
        return True

    #   rekursiver Abbruch
    if (remaining_value < 1):
        return False

    last_digit = remaining_value % 10
    new_current = current_value * 10 + last_digit
    new_remaining = remaining_value // 10

    print("last_digit: %d, new_current: %d, new_remaining: %d" %
          (last_digit, new_current, new_remaining))

    return __is_number_palindrome_rec_helper(original_number, new_current,
                                             new_remaining)


def main():
    print("121", is_number_palindrome(121))
    # print("010", isNumberPalindrome(010))
    print("101", is_number_palindrome(101))
    print("10101", is_number_palindrome(10101))

    # darf keine Nullen enthalten
    # print(isNumberPalindrome(102343201))
    print("1234321", is_number_palindrome(1234321))

    print("---------------------------------")

    print("121", is_number_palindrome_rec(121))
    print("122", is_number_palindrome_rec(122))
    print("10101", is_number_palindrome_rec(10101))
    print("1234321", is_number_palindrome_rec(1234321))
    print("102343201", is_number_palindrome_rec(102343201))


if __name__ == "__main__":
    main()
