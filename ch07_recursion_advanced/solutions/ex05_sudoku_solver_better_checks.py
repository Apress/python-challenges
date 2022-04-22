# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch06_arrays.intro.intro import print_array


##################################################

def solve_sudoku(board):
    return solve_sudoku_helper(board, 0, 0)


def solve_sudoku_helper(board, start_row, start_col):
    # 1) Bereits alle Zeilen bearbeitet?
    if start_row > 8:
        return True

    row = start_row
    col = start_col

    # überspringe so lange Felder mit Zahlen, bis wir auf ein Leerfeld stoßen
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
        if is_valid_position(board, row, col):

            # 4b) Rekursiver Abstieg für das Nachfolgefeld
            if (col < 8):
                # rekursiver Abstieg: nächstes          Feld in X - Richtung
                solved = solve_sudoku_helper(board, row, col + 1)
            else:
                # rekursiver Abstieg: nächstes Feld in neuer Zeile
                solved = solve_sudoku_helper(board, row + 1, 0)

            # 4c) Backtracking, wenn Rekursion nicht erfolgreich
            if (not solved):
                # Backtrack: keine Lösunggefunden
                board[row][col] = 0
            else:
                return True

        else:
            # Nächste Ziffer probieren
            board[row][col] = 0

    return False


# Optimization 1

def is_valid_position(board, row, col):
    return check_single_horizontally(board, row) and \
           check_single_vertically(board, col) and \
           check_single_box(board, row, col)


def check_single_horizontally(board, row):
    column_values = [board[row][col] for col in range(9)]

    return all_desired_numbers(column_values)


def check_single_vertically(board, col):
    row_values = [board[row][col] for row in range(9)]

    return all_desired_numbers(row_values)


def check_single_box(board, row, col):
    box_values = collect_box_values(board, row // 3, col // 3)

    return all_desired_numbers(box_values)


def collect_box_values(board, y_box, x_box):
    box_values = []

    # innerhalb der Boxen jeweils 3 x 3
    for y in range(3):
        for x in range(3):
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


def remove_all_occurences(the_list, val):
    return [value for value in the_list if value != val]


def main():
    board1 = [[1, 2, 0, 4, 5, 0, 7, 8, 9],
             [0, 5, 6, 7, 0, 9, 0, 2, 3],
             [7, 8, 0, 1, 2, 3, 4, 5, 6],
             [2, 1, 4, 0, 6, 0, 8, 0, 7],
             [3, 6, 0, 8, 9, 7, 2, 1, 4],
             [0, 9, 7, 0, 1, 4, 3, 6, 0],
             [5, 3, 1, 6, 0, 2, 9, 0, 8],
             [6, 0, 2, 9, 7, 8, 5, 3, 1],
             [9, 7, 0, 0, 3, 1, 6, 4, 2]]

    if solve_sudoku(board1):
        print("Solved!")
    print_array(board1)

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
