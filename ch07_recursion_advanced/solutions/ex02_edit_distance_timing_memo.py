# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import time

from ch07_recursion_advanced.solutions.ex02_edit_distance import edit_distance_optimized


def main():
    inputs_tuples = [["Micha", "Michael"],
                     ["rapple", "tables"],
                     ["sunday-Morning", "saturday-Night"],
                     ["sunday-Morning-Breakfast", "saturday-Night-Party"]]

    for inputs in inputs_tuples:
        start = time.process_time()
        result = edit_distance_optimized(inputs[0], inputs[1])
        end = time.process_time()

        print(inputs[0] + " -> " + inputs[1] + " edits: ", result)

        print("edit_distance_optimized took %.2f ms" % ((end - start) * 1000))


if __name__ == "__main__":
    main()

