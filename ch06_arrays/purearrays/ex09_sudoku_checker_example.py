# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch06_arrays.solutions.ex09_sudoku_checker import check_vertically, check_horizontally, check_boxes, is_sudoku_valid

import numpy as np

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

    print("V: ", check_vertically(np.array(board)))
    print("H: ", check_horizontally(np.array(board)))
    print("B: ", check_boxes(np.array(board)))
    print("S: ", is_sudoku_valid(np.array(board)))

    board2 = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
              [4, 0, 0, 7, 8, 9, 1, 2, 3],
              [7, 8, 9, 1, 2, 3, 4, 5, 6],
              [2, 1, 4, 3, 6, 0, 8, 9, 7],
              [3, 6, 5, 8, 9, 7, 2, 1, 4],
              [8, 9, 0, 2, 1, 4, 3, 6, 5],
              [5, 3, 0, 6, 4, 2, 0, 7, 8],
              [6, 4, 2, 9, 0, 8, 5, 3, 1],
              [9, 0, 0, 5, 3, 1, 6, 4, 2], ]

    print("V: ", check_vertically(np.array(board2)))
    print("H: ", check_horizontally(np.array(board2)))
    print("B: ", check_boxes(np.array(board2)))
    print("S: ", is_sudoku_valid(np.array(board2)))


if __name__ == "__main__":
    main()



