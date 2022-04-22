# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


# Helpers


def remove_all_occurences(values, item):
    return list(filter(lambda x: x != item, values))


def all_desired_numbersV1(all_collected_values):
    if len(all_collected_values) != 9:
        raise ValueError("not 9 values to process")

    one_to_nine = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    values_set = set(all_collected_values)

    return one_to_nine == values_set


def all_desired_numbers(all_collected_values):
    # Leerfelder raus
    relevant_values = remove_all_occurences(all_collected_values, 0)

    # Prüfe auf keine Duplikate?
    values_set = set(relevant_values)

    if len(relevant_values) != len(values_set):
        return False

    # nur 1 bis 9?
    one_to_nine = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    return one_to_nine.issuperset(values_set)


def is_valid_position_v1(board):
    return check_horizontally(board) and \
           check_vertically(board) and \
           check_boxes(board)


# Langsam
def is_valid_position_v2(board, row, col):
    return check_single_horizontally(board, row) and \
           check_single_vertically(board, col) and \
           check_single_box(board, row, col)


# nur gültige Wege beschreiten, immer prüfen, ob Ziffer ein
# gültiger Kandidat ist
def is_valid_position(board, row, col, num):
    return check_num_not_in_column(board, col, num) and \
           check_num_not_in_row(board, row, num) and \
           check_num_not_in_box(board, row, col, num)


def check_num_not_in_row(board, row, num):
    for col in range(0, 9):
        if (board[row][col] == num):
            return False

    return True


def check_num_not_in_column(board, col, num):
    for row in range(0, 9):
        if board[row][col] == num:
            return False

    return True


def check_num_not_in_box(board, row, col, num):
    adjusted_row = row // 3 * 3
    adjusted_col = col // 3 * 3

    for y in range(0, 3):
        for x in range(0, 3):
            if board[adjusted_row + y][adjusted_col + x] == num:
                return False

    return True


####################################


def check_single_vertically(board, col):
    # collect all values from one row into a list
    row_values = []

    for y in range(0, 9):
        row_values.add(board[y][col])

    if not all_desired_numbers(row_values):
        return False

    return True


# check horizontally
def check_single_horizontally(board, row):
    # collect all values from one column into a list
    column_values = []

    for x in range(0, 9):
        column_values.add(board[row][x])

    if not all_desired_numbers(column_values):
        return False

    return True


def check_single_box(board, row, col):
    # Werte pro Box
    box_values = collect_single_box_values(board, row // 3, col // 3)

    if not all_desired_numbers(box_values):
        return False

    return True


def collect_single_box_values(board, y_box, x_box):
    box_values = []

    # innerhalb der Boxen jeweils 3 x 3 Felder
    for y in range(3):
        for x in range(3):
            # real idx
            real_y = y_box * 3 + y
            real_x = x_box * 3 + x

            box_values.add(board[real_y][real_x])

    return box_values


def check_horizontally(board):
    for row in range(9):
        row_values = [board[row][x] for x in range(9)]

        if not all_desired_numbers(row_values):
            return False

    return True


def check_vertically(board):
    for x in range(9):
        column_values = [board[row][x] for row in range(9)]

        if not all_desired_numbers(column_values):
            return False

    return True


def check_boxes(board):
    for y_box in range(3):
        for x_box in range(3):
            box_values = collect_box_values(board, y_box, x_box)

            if not all_desired_numbers(box_values):
                return False

    return True


def collect_box_values(board, y_box, x_box):
    box_values = []

    # innerhalb der Boxen jeweils 3 x 3
    for y in range(3):
        for x in range(3):
            # real idx
            real_y = y_box * 3 + y
            real_x = x_box * 3 + x

            box_values.append(board[real_y][real_x])

    return box_values


def is_sudoku_valid(board):
    return check_vertically(board) and check_horizontally(board) and check_boxes(board)


def main():
    board = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
             [4, 5, 6, 7, 8, 9, 1, 2, 3],
             [7, 8, 9, 1, 2, 3, 4, 5, 6],
             [2, 1, 4, 3, 6, 5, 8, 9, 7],
             [3, 6, 5, 8, 9, 7, 2, 1, 4],
             [8, 9, 7, 2, 1, 4, 3, 6, 5],
             [5, 3, 1, 6, 4, 2, 9, 7, 8],
             [6, 4, 2, 9, 7, 8, 5, 3, 1],
             [9, 7, 8, 5, 3, 1, 6, 4, 2], ]

    print("V: ", check_vertically(board))
    print("H: ", check_horizontally(board))
    print("B: ", check_boxes(board))
    print("S: ", is_sudoku_valid(board))

    board2 = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
              [4, 0, 0, 7, 8, 9, 1, 2, 3],
              [7, 8, 9, 1, 2, 3, 4, 5, 6],
              [2, 1, 4, 3, 6, 0, 8, 9, 7],
              [3, 6, 5, 8, 9, 7, 2, 1, 4],
              [8, 9, 0, 2, 1, 4, 3, 6, 5],
              [5, 3, 0, 6, 4, 2, 0, 7, 8],
              [6, 4, 2, 9, 0, 8, 5, 3, 1],
              [9, 0, 0, 5, 3, 1, 6, 4, 2], ]

    print("V: ", check_vertically(board2))
    print("H: ", check_horizontally(board2))
    print("B: ", check_boxes(board2))
    print("S: ", is_sudoku_valid(board2))


if __name__ == "__main__":
    main()
