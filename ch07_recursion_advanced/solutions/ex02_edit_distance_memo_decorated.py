# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch07_recursion_advanced.intro.decorator_utils import decorate_with_memo_shorter


def edit_distance(str1, str2):
    return __edit_distance_helper(str1.lower(), str2.lower(),
                                  len(str1) - 1, len(str2) - 1)


@decorate_with_memo_shorter
def __edit_distance_helper(str1, str2, pos1, pos2):
    # rekursiver Abbruch
    # wenn einer der Strings am Anfang ist und der andere
    # noch nicht, dann nimm die Länge des verbliebenen Strings
    if pos1 < 0:
        return pos2 + 1

    if pos2 < 0:
        return pos1 + 1

    # Prüfe, ob die Zeichen übereinstimmen und dann auf zum nächsten
    if str1[pos1] == str2[pos2]:
        # rekursiver Abstieg
        return __edit_distance_helper(str1, str2, pos1 - 1, pos2 - 1)
    else:
        # prüfe auf insert, delete, change
        insert_in_first = __edit_distance_helper(str1, str2, pos1, pos2 - 1)
        delete_in_first = __edit_distance_helper(str1, str2, pos1 - 1, pos2)
        change = __edit_distance_helper(str1, str2, pos1 - 1, pos2 - 1)

        # Minimum aus allen drei Varianten + 1
        return 1 + min(insert_in_first, delete_in_first, change)


def main():
    inputs_tuples = [("Micha", "Michael"),
                     ("rapple", "tables"),
                     ("maple", "tables"),
                     ("sunday-Night-Mic", "saturday-Morning-Mi"),
                     ("sunday-Night-Mike", "saturday-Morning-Micha")]

    print("With memoization")
    for inputs in inputs_tuples:
        print(inputs[0], " -> ", inputs[1],
              " edits: ", str(edit_distance(inputs[0], inputs[1])))


if __name__ == "__main__":
    main()
