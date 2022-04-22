# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


names1 = ["Micha", "Tim", "Tom", "Willi"]
names2 = ["Marcello", "Karthi", "Michael"]

names = names1 + names2

print(names) # ['Micha', 'Tim', 'Tom', 'Willi', 'Marcello', 'Karthi', 'Michael']
print(names[-1]) # Michael
print(names[::-1]) # ['Michael', 'Karthi', 'Marcello', 'Willi', 'Tom', 'Tim', 'Micha']
print(names[::2]) # ['Micha', 'Tom', 'Marcello', 'Michael']

print("len: %d, min: %s, max: %s" % (len(names), min(names), max(names)))



#################################################
print("------------- LIST OPERATIONS ---------")

numbers = [1, 2, 3, 4]
names = ["Peter", "Tim", "Mike", "Tom", "Mike"]

names.append("Tom")
names.insert(1, "Carsten")
names.remove("Tom")
print(names)

names.extend(numbers)
names.reverse()
print(names)

print("pop:", names.pop())
print("Tom idx:", names.index("Tom"))
print("Mike count:", names.count("Mike"))


list = [ "Micha", "tim", "Micha", "Tom"]
list[1] = "TIM"
print(list)

last_index_of = lambda values, item: len(values) - values[::-1].index(item) - 1
print(last_index_of(list, "Micha"))

def rindex(values, item):
    reversed_values = values[::-1]
    return len(values) - reversed_values.index(item) - 1

print(rindex(list, "Micha"))


names = ["Peter", "Tom", "Mike"]
names = names + names
print(names)
names = names * 2
print(names)

tupel = ("Peter", 3, "Zürich")
tupel = tupel + tupel
print(tupel)
tupel = tupel * 2
print(tupel)


iterator = iter(names)
while True:
    try:
        name = next(iterator)
    except StopIteration:
        break
    print(name, end=" ")
print()

backiterator = reversed(names)
while True:
    try:
        name = next(backiterator)
    except StopIteration:
        break
    print(name, end=" ")
print()
