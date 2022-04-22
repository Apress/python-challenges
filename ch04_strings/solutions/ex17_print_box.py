# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def print_box(width, height, fillchar):
    for y in range(height):
        for x in range(width):
            if x == 0 and (y == 0 or y == height - 1):
                print("+", end="")
            elif x == width - 1 and (y == 0 or y == height - 1):
                print("+", end="")
            elif y == 0 or y == height - 1:
                print("-", end="")
            elif x == 0 or x == width - 1:
                print("|", end="")
            else:
                print(fillchar, end="")
        print()


def main():
    print_box(7, 5, "*")
    print_box(9, 7, "$")


if __name__ == "__main__":
    main()
