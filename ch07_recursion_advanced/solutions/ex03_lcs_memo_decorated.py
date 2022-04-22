# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch07_recursion_advanced.intro.decorator_utils import decorate_with_memo_shorter


def lcs(str1, str2):
    return __lcs_helper(str1, str2, len(str1) - 1, len(str2) - 1)


@decorate_with_memo_shorter
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


def main():
    print("lcs pure recursive")
    print(lcs("ABCE", "ZACEF"))
    print(lcs("ABCXY", "XYACB"))
    print(lcs("ABCMIXCHXAEL", "MICHAEL"))
    print(lcs("MICHAELINDEN", "XMXIXCXHXAXEXLX"))
    print(lcs("sunday-Morning", "saturday-Night-Party"))


if __name__ == "__main__":
    main()
