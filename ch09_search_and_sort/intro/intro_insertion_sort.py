# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def find_insert_pos_from_current(values, current_pos):
    insert_pos = current_pos
    while insert_pos > 0 and values[insert_pos - 1] > values[current_pos]:
        insert_pos -= 1

    return insert_pos


def find_insert_pos_from_start(values, current_pos):
    insert_pos = 0
    while insert_pos < current_pos and values[insert_pos] < values[current_pos]:
        insert_pos += 1

    return insert_pos


def insertion_sort(values):
    for current_pos in range(1, len(values)):
        current_val = values[current_pos]
        insert_pos = find_insert_pos_from_current(values, current_pos)

        move_right(values, current_pos, insert_pos)

        values[insert_pos] = current_val


def move_right(values, current_pos, insert_pos):
    move_pos = current_pos
    while move_pos > insert_pos:
        values[move_pos] = values[move_pos - 1]
        move_pos -= 1
