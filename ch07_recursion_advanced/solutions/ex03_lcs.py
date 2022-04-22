# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def lcs(str1, str2):
    return __lcs_helper(str1, str2, len(str1) - 1, len(str2) - 1)


def __lcs_helper(str1, str2, pos1, pos2):
    # rekursiver Abbruch
    if pos1 < 0 or pos2 < 0:
        return ""

    # Sind die Zeichen gleich?
    if str1[pos1] == str2[pos2]:
        # rekursiver Abstieg
        return __lcs_helper(str1, str2, pos1 - 1, pos2 - 1) + \
               str1[pos1]
    else:
        # ansonsten nimm einen von beiden Buchstaben weg und probiere es
        # erneut, allerdings gehört keiner von beiden Buchstaben ins Ergebnis
        lcs1 = __lcs_helper(str1, str2, pos1, pos2 - 1)
        lcs2 = __lcs_helper(str1, str2, pos1 - 1, pos2)

        return lcs1 if len(lcs1) > len(lcs2) else lcs2


def lcs_from_start(str1, str2):
    return __lcs__from_start_helper(str1, str2, 0, 0)


def __lcs__from_start_helper(str1, str2, pos1, pos2):
    #  rekursiver Abbruch: Ein Text am Ende
    if pos1 >= len(str1) or pos2 >= len(str2):
        return ""

    # Sind die Zeichen gleich?
    if str1[pos1] == str2[pos2]:
        # rekursiver Abstieg
        return str1[pos1] + \
               __lcs__from_start_helper(str1, str2, pos1 + 1, pos2 + 1)

    else:
        # ansonsten nimm einen von beiden Buchstaben weg und probiere es
        # erneut, allerdings gehört keiner von beiden Buchstaben ins Ergebnis
        lcs1 = __lcs__from_start_helper(str1, str2, pos1, pos2 + 1)
        lcs2 = __lcs__from_start_helper(str1, str2, pos1 + 1, pos2)

        return lcs1 if len(lcs1) > len(lcs2) else lcs2


def lcs_optimized(str1, str2):
    values = [[None for _ in range(len(str2))] for _ in range(len(str1))]

    return __lcs_with_memo(str1, str2, len(str1) - 1, len(str2) - 1, values)


def __lcs_with_memo(str1, str2, pos1, pos2, values):
    # rekursiver Abbruch
    if pos1 < 0 or pos2 < 0:
        return ""

    # MEMOIZATION
    if values[pos1][pos2] != None:
        return values[pos1][pos2]

    lcs = ""

    # Sind die Zeichen gleich?
    if str1[pos1] == str2[pos2]:
        # rekursiver Abstieg
        lcs = __lcs_with_memo(str1, str2, pos1 - 1, pos2 - 1, values) + \
              str1[pos1]
    else:
        # ansonsten nimm einen von beiden Buchstaben weg und probiere es
        # erneut, allerdings gehört keiner von beiden Buchstaben ins Ergebnis
        lcs1 = __lcs_with_memo(str1, str2, pos1, pos2 - 1, values)
        lcs2 = __lcs_with_memo(str1, str2, pos1 - 1, pos2, values)

        lcs = lcs1 if len(lcs1) > len(lcs2) else lcs2

    # MEMOIZATION
    values[pos1][pos2] = lcs

    return lcs


def main():

    print(set("ABCA")) # {'B', 'C', 'A'}
    res = set("ABCA")
    res.update("ABCD")
    print(res) # {'B', 'C', 'A'}

    print(set(list("ABCA")))  # {'B', 'C', 'A'}
    res = set(list('ABCA'))
    res.update(list("ABCD"))
    print(res)  # {'B', 'C', 'A'}

    # Trick, um Strings in Sets zu verwalten
    print(set("ABCA",))  # {'B', 'C', 'A'}
    res = set(('ABCA',))
    res.update(("ABCD",))
    print(res)  # {'B', 'C', 'A'}

    print("lcs pure recursive")
    print(lcs("ABCE", "ZACEF"))
    print(lcs("ABCXY", "XYACB"))
    print(lcs("ABCMIXCHXAEL", "MICHAEL"))
    print(lcs("MICHAELINDEN", "XMXIXCXHXAXEXLX"))
    #print(lcs("sunday-Morning", "saturday-Night-Party"))

    print("lcs pure recursive (from start)")
    print(lcs_from_start("ABCE", "ZACEF"))
    print(lcs_from_start("ABCXY", "XYACB"))
    print(lcs_from_start("ABCMIXCHXAEL", "MICHAEL"))
    print(lcs_from_start("MICHAELINDEN", "XMXIXCXHXAXEXLX"))
    #print(lcs_from_start("sunday-Morning", "saturday-Night-Party"))

    print("lcs with memo")
    print(lcs_optimized("ABCE", "ZACEF"))
    print(lcs_optimized("ABCXY", "XYACB"))
    print(lcs_optimized("ABCMIXCHXAEL", "MICHAEL"))
    print(lcs_optimized("MICHAELINDEN", "XMXIXCXHXAXEXLX"))
    print(lcs_optimized("sunday-Morning", "saturday-Night-Party"))


if __name__ == "__main__":
    main()
