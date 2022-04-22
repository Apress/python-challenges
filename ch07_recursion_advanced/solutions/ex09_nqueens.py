# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch06_arrays.intro.intro import get_dimension


def solve_n_queens(size):
    board = initialize_board(size)
    solved = solve_n_queens_helper(board, 0)

    return solved, board  # (solved, board)


def initialize_board(size):
    return [[' ' for col in range(size)] for row in range(size)]


def solve_n_queens_helper(board, row):
    max_row, max_col = get_dimension(board)

    if row >= max_row:
        return True

    solved = False
    col = 0
    while col < max_col and not solved:
        if is_valid_position(board, col, row):
            place_queen(board, col, row)

            # recursive descent
            solved = solve_n_queens_helper(board, row + 1)

            # Backtracking, if no solution
            if not solved:
                remove_queen(board, col, row)

        col += 1

    return solved


def place_queen(board, col, row):
    board[row][col] = 'Q'


def remove_queen(board, col, row):
    board[row][col] = ' '


def is_valid_position(board, col, row):
    max_row, max_col = get_dimension(board)

    return check_horizontally(board, row, max_col) and \
           check_vertically(board, col, max_row) and \
           check_diagonally_left_up(board, col, row) and \
           check_diagonally_right_up(board, col, row, max_col)


def check_horizontally(board, row, max_col):
    col = 0
    while col < max_col and board[row][col] == ' ':
        col += 1

    return col >= max_col


def check_vertically(board, col, max_roy):
    row = 0
    while row < max_roy and board[row][col] == ' ':
        row += 1

    return row >= max_roy


def check_diagonally_right_up(board, col, row, max_col):
    diag_ru_free = True

    while col < max_col and row >= 0:
        diag_ru_free = diag_ru_free and board[row][col] == ' '
        row -= 1
        col += 1

    return diag_ru_free


def check_diagonally_left_up(board, col, row):
    diag_lu_free = True

    while col >= 0 and row >= 0:
        diag_lu_free = diag_lu_free and board[row][col] == ' '
        row -= 1
        col -= 1

    return diag_lu_free


def print_board(values):
    line = "-" * (len(values[0]) * 2 + 1)
    print(line)

    for y in range(len(values)):
        print("|", end='')
        for x in range(len(values[y])):
            print(values[y][x], end='|')

        print()
        print(line)


def solve_and_print(size):
    solved_and_board = solve_n_queens(size)

    if solved_and_board[0]:
        print_board(solved_and_board[1])


def main():
    solve_and_print(4)
    solve_and_print(8)


if __name__ == "__main__":
    main()
