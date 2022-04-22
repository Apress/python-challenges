# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from enum import Enum, auto

from ch05_datastructures.solutions.ex02_stack import Stack


def check_parentheses(input):
    # Ungerade Länge kann keine wohlgeformte Klammerung sein
    if len(input) % 2 != 0:
        return False

    opening_parentheses = Stack()

    for current_char in input:
        if is_opening_parenthesis(current_char):
            opening_parentheses.push(current_char)
        elif is_closing_parenthesis(current_char):
            if opening_parentheses.is_empty():
                # Schließende vor öffnender Klammer
                return False

            last_opening_parens = opening_parentheses.pop()
            if not is_matching_parenthesis_pair(last_opening_parens, current_char):
                # Unterschiedliche Klammerpaare
                return False
        else:
            # Ungültiges Zeichen
            return False

    return opening_parentheses.is_empty()


def check_parentheses_v2(input):
    # Ungerade Länge kann keine wohlgeformte Klammerung sein
    if len(input) % 2 != 0:
        return CheckResult.ODD_LENGTH

    opening_parentheses = Stack()

    for current_char in input:
        if is_opening_parenthesis(current_char):
            opening_parentheses.push(current_char)
        elif is_closing_parenthesis(current_char):
            if opening_parentheses.is_empty():
                return CheckResult.CLOSING_BEFORE_OPENING

            last_opening_parens = opening_parentheses.pop()
            if not is_matching_parenthesis_pair(last_opening_parens, current_char):
                return CheckResult.MISMATCHING_PARENTHESIS
        else:
            return CheckResult.INVALID_CHAR

    if opening_parentheses.is_empty():
        return CheckResult.OK

    return CheckResult.REMAINING_OPENING


# Helpers
def is_opening_parenthesis(ch):
    return ch == '(' or ch == '[' or ch == '{'
    # Schönere Alternative:
    #return ch in ["(","[","{"]


def is_closing_parenthesis(ch):
    return ch in [")","]","}"]


def is_matching_parenthesis_pair(opening, closing):
    return (opening == '(' and closing == ')') or \
           (opening == '[' and closing == ']') or \
           (opening == '{' and closing == '}')
    # Alternative Tupel-Schreibweise
    # return (opening, closing) in [ ('(', ')'), ('[', ']'), ('{', '}')]


class CheckResult(Enum):
    OK = auto()
    ODD_LENGTH = auto()
    CLOSING_BEFORE_OPENING = auto()
    MISMATCHING_PARENTHESIS = auto()
    INVALID_CHAR = auto()
    REMAINING_OPENING = auto()


def main():
    print(check_parentheses("(())"))
    print(check_parentheses("({[]})"))
    print(check_parentheses("((())"))

    print(check_parentheses_v2("}())"))
    print(check_parentheses_v2("()}())"))
    print(check_parentheses_v2("(())"))
    print(check_parentheses_v2("({[]})"))
    print(check_parentheses_v2("((())"))
    print(check_parentheses_v2("((}())"))
    print(check_parentheses_v2("}())"))
    print(check_parentheses_v2("(a))"))
    print(check_parentheses_v2("()(("))
    print(check_parentheses_v2("()(("))


if __name__ == "__main__":
    main()
