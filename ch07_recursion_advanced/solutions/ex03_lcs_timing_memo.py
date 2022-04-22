# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import time

from ch07_recursion_advanced.solutions.ex03_lcs import lcs_optimized


def main():
    inputs_tuples = [["ABCMIXCHXAEL", "MICHAEL"],
                     ["sunday-Morning", "saturday-Night-Party"],
                     ["sunday-Morning-Wakeup", "saturday-Night"]]

    for inputs in inputs_tuples:
        start = time.process_time()
        result = lcs_optimized(inputs[0], inputs[1])
        end = time.process_time()

        print(inputs[0] + " -> " + inputs[1] + " lcs:", result)
        print("lcs_optimized took %.2f ms" % ((end - start) * 1000))


if __name__ == "__main__":
    main()
