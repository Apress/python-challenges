# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def is_magic6(values):
    values_with_loop = list(values)
    values_with_loop.append(values[0])

    side1 = values_with_loop[0:3]
    side2 = values_with_loop[2:5]
    side3 = values_with_loop[4:7]

    return compare_sum_of_sides(side1, side2, side3)


def compare_sum_of_sides(side1, side2, side3):
    sum1 = sum(side1)
    sum2 = sum(side2)
    sum3 = sum(side3)

    return sum1 == sum2 and sum2 == sum3


def is_magic_triangle(values):
    if len(values) % 3 != 0:
        raise ValueError("Not a triangle: " + len(values))

    side_length = 1 + len(values) // 3

    values_with_loop = list(values)
    values_with_loop.append(values[0])

    side1 = values_with_loop[0: side_length]
    side2 = values_with_loop[side_length - 1: side_length * 2 - 1]
    side3 = values_with_loop[(side_length - 1) * 2: side_length * 3 - 2]

    return compare_sum_of_sides(side1, side2, side3)


def is_magic_triangle_v2(values):
    if len(values) % 3 != 0:
        raise ValueError("Not a triangle: " + len(values))

    side_length = 1 + len(values) // 3

    pos = 0

    sum_of_sides = [0, 0, 0]
    for current_side in range(3):
        for _ in range(side_length):
            sum_of_sides[current_side] += values[pos]

            # Trick 1: mit Modulo => keine Spezialbehandlung für letzten Wert
            pos = (pos + 1) % len(values)

        # Trick 2: die Seiten überlappen sich, Endefeld = Startfeld
        pos -= 1

    return sum_of_sides[0] == sum_of_sides[1] and \
           sum_of_sides[1] == sum_of_sides[2]


def is_magic_triangle_v3(values):
    if len(values) % 3 != 0:
        raise ValueError("Not a triangle: " + len(values))

    side_length = 1 + len(values) // 3

    sum_of_side1 = sum_of_side(values, 0 * (side_length - 1), side_length)
    sum_of_side2 = sum_of_side(values, 1 * (side_length - 1), side_length)
    sum_of_side3 = sum_of_side(values, 2 * (side_length - 1), side_length)

    return sum_of_side1 == sum_of_side2 and sum_of_side2 == sum_of_side3


def sum_of_side(values, start, side_length):
    sum = 0
    for i in range(start, start + side_length):
        sum += values[i % len(values)]

    return sum


def main():
    print(is_magic6([1, 5, 3, 4, 2, 6]))
    print(is_magic6([1, 2, 3, 4, 5, 6]))

    print(is_magic_triangle([1, 5, 3, 4, 2, 6]))
    print(is_magic_triangle([1, 2, 3, 4, 5, 6]))

    print(is_magic_triangle([2, 5, 9, 1, 6, 7, 3, 4, 8]))
    print(is_magic_triangle([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    print(is_magic_triangle_v2([2, 5, 9, 1, 6, 7, 3, 4, 8]))
    print(is_magic_triangle_v2([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    print(is_magic_triangle_v3([2, 5, 9, 1, 6, 7, 3, 4, 8]))
    print(is_magic_triangle_v3([1, 2, 3, 4, 5, 6, 7, 8, 9]))


if __name__ == "__main__":
    main()
