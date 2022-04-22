# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def remove_duplicates(input):
    result = ""
    already_seen = set()

    for current_char in input:
        if not current_char in already_seen:
            already_seen.add(current_char)
            result += current_char

    return result


def main():
    print(remove_duplicates("bananas"))
    print(remove_duplicates("lalalamama"))
    print(remove_duplicates("MICHAEL"))


if __name__ == "__main__":
    main()
