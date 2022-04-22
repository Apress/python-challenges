# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch02_math.intro.intro import find_proper_divisors


def calc_friends(max_exclusive):
    friends = {}

    for i in range(2, max_exclusive):
        divisors1 = find_proper_divisors(i)
        sum_div1 = sum(divisors1)
        divisors2 = find_proper_divisors(sum_div1)
        sum_div2 = sum(divisors2)

        if i == sum_div2 and sum_div1 != sum_div2:
            friends[i] = sum_div1

    return friends


def main():
    print("friends:", calc_friends(1500))


if __name__ == "__main__":
    main()
