# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import numpy as np

from ch06_arrays.solutions.ex03_palindrome import is_palindrome_rec, is_palindrome_iterative


def main():
    print(is_palindrome_rec(np.array(["Ein", "Test", " – ", "Test", "Ein"])))
    print(is_palindrome_rec(np.array(["Max", "Mike", "Mike", "Max"])))
    print(is_palindrome_rec(np.array(["Tim", "Tom", "Mike", "Max"])))

    print(is_palindrome_iterative(np.array(["Ein", "Test", " – ", "Test", "Ein"])))
    print(is_palindrome_iterative(np.array(["Max", "Mike", "Mike", "Max"])))
    print(is_palindrome_iterative(np.array(["Tim", "Tom", "Mike", "Max"])))


if __name__ == "__main__":
    main()
