# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import sys


def max_revenue(prices):
    relevant_mins = calc_relevant_mins(prices)
    return calc_max_revenue(prices, relevant_mins)


def calc_relevant_mins(prices):
    relevant_mins = []

    current_min = sys.maxsize
    for current_price in prices:
        current_min = min(current_min, current_price)
        relevant_mins.append(current_min)

    return relevant_mins


def calc_max_revenue(prices, relevant_mins):
    max_revenue = 0
    for i, price in enumerate(prices):
        if price > relevant_mins[i]:
            current_revenue = price - relevant_mins[i]
            max_revenue = max(max_revenue, current_revenue)

    return max_revenue


def max_revenue_optimized(prices):
    current_min = sys.maxsize
    max_revenue = 0

    for current_price in prices:
        current_min = min(current_min, current_price)
        current_revenue = current_price - current_min
        max_revenue = max(max_revenue, current_revenue)

    return max_revenue


def main():
    print(max_revenue([255, 260, 250, 240, 228, 270, 300, 210, 245]))  # 72
    print(max_revenue([0, 10, 20, 30, 40, 50, 60, 70]))  # 70
    print(max_revenue([70, 60, 50, 40, 30, 20, 10, 0]))  # 0
    print(max_revenue([]))  # 0

    print(max_revenue_optimized([255, 260, 250, 240, 228, 270, 300, 210, 245]))  # 72
    print(max_revenue_optimized([0, 10, 20, 30, 40, 50, 60, 70]))  # 70
    print(max_revenue_optimized([70, 60, 50, 40, 30, 20, 10, 0]))  # 0
    print(max_revenue_optimized([]))  # 0


if __name__ == "__main__":
    main()
