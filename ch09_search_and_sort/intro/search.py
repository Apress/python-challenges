# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


print([1, 2, 3, 2].index(2))  # => 1

print([i for i, value in enumerate([1, 2, 3, 2, 4, 2]) if value == 2])  # => [1, 3, 5]

print([1, 2, 3, 2, 4, 2].count(2))  # => 3

programmers = {"Michael": "Python",
               "Tim": "C++",
               "Karthi": "Java"}

if "Karthi" in programmers.keys():
    print("Karthi is here")

# Python-Kurzform
if "Karthi" in programmers:
    print("Karthi is here II")

if "C++" in programmers.values():
    print("someone knows C++")

if ("Michael", "Python") in programmers.items():
    print("Michael knows Python")

print(all([7, 2] in [2, 3, 5, 7, 9]))
print(any([7, 2] in [2, 3, 5, 7, 9]))
print(any([4] in [2, 3, 5, 7, 9]))
# Alternative mit mehr Flexibilität
print(all(elem in [2, 3, 5, 7, 9] for elem in [7, 2]))
print(any(elem in [2, 3, 5, 7, 9] for elem in [7, 2]))
print(any(elem in [2, 3, 5, 7, 9] for elem in [4]))

print("Hallo".rindex("l"))
print("Hallo".rfind("l"))
print("Hallo".rfind("x"))  # => -1


# print("Hallo".rindex("x")) # => ValueError: substring not found

def last_index_of(values, search_for):
    for pos in range(len(values) - 1, -1, -1):
        if values[pos] == search_for:
            return pos

    return -1


print(last_index_of([1, 2, 3, 2, 4, 2, 5, 2], 2))  # => 7

values = [0] * 13
print(values)
values[2] = 7
values[7] = 2
print(values)
