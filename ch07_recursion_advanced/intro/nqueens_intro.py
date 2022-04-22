# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch06_arrays.intro.intro import get_dimension


def solve_n_queens(size):
    board = initialize_board(size)
    solved = solve_n_queens_helper(board, 0)

    return solved, board


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

            # rekursiver Abstieg
            solved = solve_n_queens_helper(board, row + 1)

            # Backtracking, sofern keine Lösung
            if not solved:
                remove_queen(board, col, row)

    return solved


def place_queen(board, col, row):
    board[row][col] = 'Q'


def remove_queen(board, col, row):
    board[row][col] = ' '


def is_valid_position(board, col, row):
    # TODO
    return False
