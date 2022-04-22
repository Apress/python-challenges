# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from functools import reduce


def join(values, delimiter):
    result = ""
    for i, current_value in enumerate(values):
        result += current_value
        # no delimiter after last
        if i < len(values) - 1:
            result += delimiter

    return result


def join_with_reduce(values, delimiter):
    return reduce(lambda str1, str2: str1 + delimiter + str2, values)


def main():
    print(join(["Dies", "ist", "wichtig"], "-**-"))

    info = ["Dies", "ist", "wichtig"]
    separator = "-**-"
    print(separator.join(info))


if __name__ == "__main__":
    main()
