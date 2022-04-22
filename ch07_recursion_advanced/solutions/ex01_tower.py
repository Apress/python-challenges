# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch05_datastructures.solutions.ex02_stack import Stack


class Tower:
    def __init__(self, name):
        self.name = name
        self.__values = Stack()

    def __str__(self):
        return "Tower [" + self.name + "]"

    def push(self, item):
        self.__values.push(item)

    def pop(self):
        return self.__values.pop()

    def print_tower(self, max_height):
        height = self.__values.size() - 1

        visual = self.draw_top(max_height, height)
        visual += self.draw_slices(max_height, height)
        visual += self.draw_bottom(max_height)

        return visual

    def draw_top(self, max_height, height):
        visual = [" " * max_height + self.name + " " * max_height]

        for i in range(max_height - height - 1, 0, -1):
            visual.append(" " * max_height + "|" + " " * max_height)

        return visual

    def draw_slices(self, max_height, height):
        visual = []
        for i in range(height, -1, -1):
            value = self.__values.get_at(i)
            padding = max_height - value

            visual.append(" " * padding + "#" * value + "|" + "#" * value + " " * padding)

        return visual

    def draw_bottom(self, height):
        return ["-" * (height * 2 + 1)]
