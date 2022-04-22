# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def calc(m, n):
    return m * n // 2 % 7


def calc_v2(m, n):
    return int(m * n / 2) % 7


def calc_sum_and_count_all_numbers_div_by_2_or_7(max_exclusive):
    count = 0
    sum = 0

    for i in range(1, max_exclusive):
        if i % 2 == 0 or i % 7 == 0:
            count += 1
            sum += i

    print("count:", count)
    print("sum:", sum)


def calc_sum_and_count_all_numbers_div_by_2_or_7_v2(max_exclusive):
    count = 0
    sum = 0

    for i in range(1, max_exclusive):
        is_divisible_by2or7 = i % 2 == 0 or i % 7 == 0
        if is_divisible_by2or7:
            count += 1
            sum += i

    return {"sum": sum, "count": count}
    # return ReturnCode(sum, count)


class ReturnCode:
    def __init__(self, sum, count):
        self.sum = sum
        self.count = count

    def __eq__(self, other):
        return self.sum == other.sum and \
               self.count == other.count

    def __str__(self):
        return "sum: " + str(self.sum) + " / count: " + str(self.count)


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 != 0


def main():
    print(calc(6, 7))  # 0
    print(calc(3, 4))  # 6
    print(calc(5, 5))  # 5

    calc_sum_and_count_all_numbers_div_by_2_or_7(15)
    print(calc_sum_and_count_all_numbers_div_by_2_or_7(10))
    print(calc_sum_and_count_all_numbers_div_by_2_or_7_v2(4))
    print(calc_sum_and_count_all_numbers_div_by_2_or_7_v2(8))

    print("is_even:", is_even(7))
    print("is_odd:", is_odd(7))
    print("is_odd:", is_odd(-7))


if __name__ == "__main__":
    main()
