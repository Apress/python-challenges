# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


color_set = {"RED", "GREEN", "BLUE"}
color_set.update(["YELLOW", "ORANGE"])
color_set.add("GOLD")

print(color_set)


number_set1 = {1, 2, 3, 4, 5, 6, 7, 8}
number_set2 = {2, 3, 5, 7, 9, 11, 13}

print("union: %s\nintersection: %s\ndiff 1-2: %s\nsym diff: %s" %
      ((number_set1 | number_set2),
       (number_set1 & number_set2),
       (number_set1 - number_set2),
       (number_set1 ^ number_set2)))
