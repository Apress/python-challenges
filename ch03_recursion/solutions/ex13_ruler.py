# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length, "")
        draw_interval(center_length - 1)


def draw_line(count, label):
    print(("-" * count) + " " + str(label))


def draw_ruler(major_tick_count, max_length):
    draw_line(max_length, "0")

    for i in range(1, major_tick_count + 1):
        draw_interval(max_length - 1)
        draw_line(max_length, i)


def main():
    draw_ruler(3, 4)


if __name__ == "__main__":
    main()
