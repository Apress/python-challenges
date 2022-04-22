# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def count_substrings(input, value_to_find):
    # rekursiver Abbruch
    if len(input) < len(value_to_find):
        return 0

    count = 0
    remaining = ""

    #   startet der Text mit der Suchzeichenfolge?
    if input.startswith(value_to_find):
        # Treffer: Setze die Suche nach dem gefundenen
        # Begriff nach der Fundstelle fort
        remaining = input[len(value_to_find):]
        count = 1
    else:
        # entferne erstes Zeichen und suche erneut
        remaining = input[1:]

    # rekursiver Abstieg
    return count_substrings(remaining, value_to_find) + count


def count_substrings_v2(input, value_to_find):
    # rekursiver Abbruch
    if len(input) < len(value_to_find):
        return 0

    # startet der Text mit der Suchzeichenfolge?
    count = 1 if input.startswith(value_to_find) else 0

    # entferne erstes Zeichen und suche erneut
    remaining = input[1:]

    # rekursiver Abstieg
    return count_substrings_v2(remaining, value_to_find) + count


def count_substrings_optimized(input, value_to_find):
    return count_substrings_helper(input, value_to_find, 0)


def count_substrings_helper(input, value_to_find, left):
    if len(input) - left < len(value_to_find):
        return 0

    count = 1 if input.startswith(value_to_find, left) else 0

    if input.startswith(value_to_find, left):
        left += len(value_to_find)
    else:
        left += 1

    return count_substrings_helper(input, value_to_find, left) + count


def main():
    print(count_substrings("xhixhix", "x"))  # 3
    print(count_substrings("xhixhix", "hi"))  # 2
    print(count_substrings("mic", "mic"))  # 1
    print(count_substrings("haha", "ho"))  # 0
    print(count_substrings("xxxxyz", "xx"))  # 2

    print("-----------------")
    print(count_substrings_v2("xhixhix", "x"))  # 3
    print(count_substrings_v2("xhixhix", "hi"))  # 2
    print(count_substrings_v2("mic", "mic"))  # 1
    print(count_substrings_v2("haha", "ho"))  # 0
    print(count_substrings_v2("xxxxyz", "xx"))  # 3

    print("-----------------")
    print(count_substrings_optimized("xhixhix", "x"))  # 3
    print(count_substrings_optimized("xhixhix", "hi"))  # 2
    print(count_substrings_optimized("mic", "mic"))  # 1
    print(count_substrings_optimized("haha", "ho"))  # 0
    print(count_substrings_optimized("xxxxyz", "xx"))  # 2

    print("-----------------")
    print("-----------------")
    print("xhixhix".count("x"))
    print("xhixhix".count("hi"))
    print("mic".count("mic"))
    print("haha".count("ho"))
    print("xxxxyz".count("xx"))



if __name__ == "__main__":
    main()
