# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


values = [1, 2, 3, 4, 5, 6, 7]

for n in range(len(values) -1, -1, -1):
    print(values[n])

for val in reversed(values):
    print(val)

for n in values[::-1]:
    print(n)

