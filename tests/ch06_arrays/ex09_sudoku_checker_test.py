# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

from ch06_arrays.solutions.ex09_sudoku_checker import is_sudoku_valid

def create_initialized_board():
    return [[1, 2, 0, 4, 5, 0, 7, 8, 9],
            [0, 5, 6, 7, 0, 9, 0, 2, 3],
            [7, 8, 0, 1, 2, 3, 4, 5, 6],
            [2, 1, 4, 0, 6, 0, 8, 0, 7],
            [3, 6, 0, 8, 9, 7, 2, 1, 4],
            [0, 9, 7, 0, 1, 4, 3, 6, 0],
            [5, 3, 1, 6, 0, 2, 9, 0, 8],
            [6, 0, 2, 9, 7, 8, 5, 3, 1],
            [9, 7, 0, 0, 3, 1, 6, 4, 2]]


def test_is_sudoku_valid():
    board = create_initialized_board()

    is_valid_sudoku = is_sudoku_valid(board)

    assert is_valid_sudoku == True


def test_is_sudoku_valid_for_invalid_board():
    board = create_initialized_board()
    # verändere es und mache es damit ungültig
    board[0][2] = 2

    is_valid_sudoku = is_sudoku_valid(board)

    assert is_valid_sudoku == False



