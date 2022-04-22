# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch06_arrays.intro.intro import print_array


def solve_sudoku(board):
    return solve_sudoku_helper(board, 0, 0)


def solve_sudoku_helper(board, start_row, start_col):
    # 1) Bereits alle Zeilen bearbeitet?
    if start_row > 8:
        return True

    row = start_row
    col = start_col

    # 2) Überspringe so lange Felder mit Zahlen, bis wir auf ein Leerfeld stoßen
    while board[row][col] != 0:
        col += 1
        if col > 8:
            col = 0
            row += 1

            # 3) Bereits alle Zeilen bearbeitet?
            if row > 8:
                return True

    solved = False

    # 4) Probiere für das aktuelle Feld alle Ziffern von 1 bis 9 durch
    for num in range(1, 10):
        board[row][col] = num

        # 4a) Prüfe, ob das gesamte Spielfeld mit der Ziffer noch gültig ist
        if is_valid_position(board):

            # 4b) Rekursiver Abstieg für das Nachfolgefeld
            if col < 8:
                # rekursiver Abstieg: nächstes Feld in x-Richtung
                solved = solve_sudoku_helper(board, row, col + 1)
            else:
                # rekursiver Abstieg: nächstes Feld in neuer Zeile
                solved = solve_sudoku_helper(board, row + 1, 0)

            # 4c) Backtracking, wenn Rekursion nicht erfolgreich
            if not solved:
                # Backtrack: keine Lösunggefunden
                board[row][col] = 0
            else:
                return True
        else:
            # Nächste Ziffer probieren
            board[row][col] = 0

    return False


def is_valid_position(board):
    return check_horizontally(board) and \
           check_vertically(board) and \
           check_boxes(board)


def check_horizontally(board):
    for row in range(9):
        # Alle Werte einer Zeile in einer Liste aufsammeln
        row_values = [board[row][x] for x in range(9)]

        if not all_desired_numbers(row_values):
            return False

    return True


def check_vertically(board):
    for x in range(9):
        # Alle Werte einer Spalte in einer Liste aufsammeln
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


def all_desired_numbers(all_collected_values):
    relevant_values = list(all_collected_values)

    # Leerfelder raus
    relevant_values = remove_all_occurences(relevant_values, 0)

    # Prüfe auf keine Duplikate?
    values_set = set(relevant_values)

    if len(relevant_values) != len(values_set):
        return False

    # nur 1 bis 9?
    return {1, 2, 3, 4, 5, 6, 7, 8, 9}.issuperset(values_set)


def remove_all_occurences(values, val):
    return [value for value in values if value != val]


def is_sudoku_valid(board):
    return check_vertically(board) and check_horizontally(board) and check_boxes(board)


def main():
    board = [[1, 2, 0, 4, 5, 0, 7, 8, 9],
             [0, 5, 6, 7, 0, 9, 0, 2, 3],
             [7, 8, 0, 1, 2, 3, 4, 5, 6],
             [2, 1, 4, 0, 6, 0, 8, 0, 7],
             [3, 6, 0, 8, 9, 7, 2, 1, 4],
             [0, 9, 7, 0, 1, 4, 3, 6, 0],
             [5, 3, 1, 6, 0, 2, 9, 0, 8],
             [6, 0, 2, 9, 7, 8, 5, 3, 1],
             [9, 7, 0, 0, 3, 1, 6, 4, 2]]

    print(board)
    print("V: ", check_vertically(board))
    print("H: ", check_horizontally(board))
    print("B: ", check_boxes(board))
    print("S: ", is_sudoku_valid(board))

    if solve_sudoku(board):
        print("Solved!")
    print_array(board)

    ############################

    board2 = [
        [6, 0, 2, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 3, 0, 0, 0, 8, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [5, 0, 0, 2, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 1],
        [0, 0, 0, 6, 0, 0, 0, 0, 0]
    ]

    print("-------------------------")
    if solve_sudoku(board2):
        print("Solved!")
    print_array(board2)


if __name__ == "__main__":
    main()
