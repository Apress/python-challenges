# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def check_braces(input):
    opening_count = 0

    for ch in input:
        if ch == "(":
            opening_count += 1
        elif ch == ")":
            opening_count -= 1
            if opening_count < 0:
                return False

    return opening_count == 0


def main():
    print(check_braces("(())"))
    print(check_braces("()()"))
    print(check_braces("(())))((())"))
    print(check_braces("(())((())"))
    print(check_braces("((()"))


if __name__ == "__main__":
    main()
