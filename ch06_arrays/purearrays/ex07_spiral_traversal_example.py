# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch06_arrays.solutions.ex07_spiral_traversal import spiral_traversal


def main():

    numbers = [[1, 2, 3, 4],
               [12, 13, 14, 5],
               [11, 16, 15, 6],
               [10, 9, 8, 7]]

    print(spiral_traversal(numbers))

    numbers2 = [[1, 2, 3, 4, 5],
                [14, 15, 16, 17, 6],
                [13, 20, 19, 18, 7],
                [12, 11, 10, 9, 8]]

    print(spiral_traversal(numbers2))



    letter_pairs = [["AB", "BC", "CD", "DE"],
                   ["JK", "KL", "LM", "EF"],
                   ["IJ", "HI", "GH", "FG"]]

    print(spiral_traversal(letter_pairs))


if __name__ == "__main__":
    main()
