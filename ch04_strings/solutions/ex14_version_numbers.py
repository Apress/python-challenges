# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def compare(val1, val2):
    if val1 < val2:
        return "<"
    if val1 > val2:
        return ">"
    return "="


def compare_versions(version1, version2):
    v1_numbers = version1.split(".")
    v2_numbers = version2.split(".")

    pos = 0
    compare_result = "="

    while (pos < len(v1_numbers) and
           pos < len(v2_numbers) and compare_result == "="):

        current_v1 = int(v1_numbers[pos])
        current_v2 = int(v2_numbers[pos])

        compare_result = compare(current_v1, current_v2)
        pos += 1

    # Gleicher Beginn etwa 3.1 und 3.1.7
    if compare_result == "=":
       return compare(len(v1_numbers), len(v2_numbers))

    return compare_result


def main():
    print(compare_versions("1.11.17", "2.3.5"))
    print(compare_versions("2.1", "2.1.3"))
    print(compare_versions("2.3.5", "2.4"))
    print(compare_versions("3.1", "2.4"))
    print(compare_versions("3.3", "3.2.9"))
    print(compare_versions("7.2.71", "7.2.71"))


if __name__ == "__main__":
    main()
