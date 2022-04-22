# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch06_arrays.solutions.ex05_jewels_board_init import init_jewels_board, check_board_validity
from ch06_arrays.intro.intro import print_array


def main():
    # Terminiert ggf. nicht!! wenn nur 1-3 möglich sind
    print("Init 10 x 5 * 3")
    print_array(init_jewels_board(10, 5, 4))

    print("Init 15 x 7 * 5")
    print_array(init_jewels_board(15, 7, 5))

    ###############################

    values_with_errors = [[2, 3, 3, 4, 4, 3, 2],
                          [1, 3, 3, 1, 3, 4, 4],
                          [4, 1, 4, 3, 3, 1, 3],
                          [2, 2, 1, 1, 2, 3, 2],
                          [3, 2, 4, 4, 3, 3, 4]]

    print_array(values_with_errors)
    print(check_board_validity(values_with_errors))


if __name__ == "__main__":
    main()
