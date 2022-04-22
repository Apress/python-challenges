# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def calc_pascal(row, col):
    # rekursiver Abbruch: Spitze
    if col == 1 and row == 1:
        return 1

    # rekursiver Abbruch: Ränder
    if col == 1 or col == row:
        return 1

    # rekursiver Abstieg
    return calc_pascal(row - 1, col) + calc_pascal(row - 1, col - 1)


def print_pascal(n):
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print(calc_pascal(row, col), end=' ')

        print()


def calc_pascal_with_action(n, action):
    # rekursiver Abbruch
    if n == 1:
        if action:
            action([1])
        return [1]
    else:
        # rekursiver Abstieg
        previous_line_values = calc_pascal_with_action(n - 1, action)

        new_line = calc_line(previous_line_values)

        if action:
            action(new_line)

        return new_line


def calc_line(previous_line):
    current_line = []
    current_line.append(1)

    for i in range(len(previous_line) - 1):
        # Wert ergibt sich aus den zwei Werten der Vorgängerzeile
        new_value = previous_line[i] + previous_line[i + 1]
        current_line.append(new_value)

    current_line.append(1)
    return current_line


def main():
    print_pascal(5)

    calc_pascal_with_action(7, print)


if __name__ == "__main__":
    main()
