# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def solve_n_queens(size):
    board = []
    solved = __solve_n_queens_helper(board, 0, size)

    return solved, board  # (solved, board)


def __solve_n_queens_helper(board, row, size):
    # rekursiver Abbruch
    if row >= size:
        return True

    solved = False
    col = 0
    while col < size and not solved:
        if __is_valid_position(board, col, row, size):
            __place_queen(board, col, row)

            # rekursiver Abstieg
            solved = __solve_n_queens_helper(board, row + 1, size)

            # Backtracking, sofern keine Lösung
            if not solved:
                __remove_queen(board, col, row)

        col += 1

    return solved


def __place_queen(board, col, row):
    if len(board) != row:
        raise ValueError("invalid row" + str(row) + " col: " + str(col))

    board.append(col)


def __remove_queen(board, col, row):
    if board[row] != col:
        raise ValueError("invalid col" + str(col) + " row: " + str(row))

    board.remove(col)


def __is_valid_position(board, col, row, size):
    yfree = not col in board

    return yfree and __check_diagonally(board, col, row, size)


def __check_diagonally(board, col, row, size):
    diag_lu_free = True
    diag_ru_free = True

    for y in range(row):
        x_pos_lu = col - (row - y)
        x_pos_ru = col + (row - y)

        if x_pos_lu >= 0:
            diag_lu_free = diag_lu_free and board[y] != x_pos_lu

        if x_pos_ru < size:
            diag_ru_free = diag_ru_free and board[y] != x_pos_ru

    return diag_ru_free and diag_lu_free


def print_board(board, size):
    line = "-" * (size * 2 + 1)
    print(line)

    for y in range(size):
        print("|", end='')
        for x in range(size):
            value = 'Q' if x == board[y] else ' '
            print(value, end='|')

        print("\n" + line)


def solve_and_print(size):
    solved_and_board = solve_n_queens(size)

    if solved_and_board[0]:
        print_board(solved_and_board[1], size)


def main():
    solve_and_print(4)
    solve_and_print(8)


if __name__ == "__main__":
    main()
