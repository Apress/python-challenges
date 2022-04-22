# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden

data1 = [True, True, True, True]
data2 = [True, False, True, True]
data3 = [False, False, False, False]


def all_assigned(values):
    for val in values:
        if not val:
            return False

    return True


print(all_assigned(data1))
print(all_assigned(data2))
print(all_assigned(data3))

# The all() function returns True if all items in an iterable are true, otherwise it returns False.

print(all(data1))
print(all(data2))
print(all(data3))
