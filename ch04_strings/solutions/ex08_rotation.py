# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def contains_rotation(str1, str2):
    new_doubled_str1 = (str1 + str1).lower()

    return str2.lower() in new_doubled_str1


def main():
    print(contains_rotation("ABCD", "ABC"))
    print(contains_rotation("ABCDEF", "EFAB"))
    print(contains_rotation("BCDE", "EC"))
    print(contains_rotation("Challenge", "GECH"))


if __name__ == "__main__":
    main()
