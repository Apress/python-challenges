# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


class Stack:
    def __init__(self):
        self._values = []

    def push(self, elem):
        self._values.append(elem)

    def pop(self):
        if self.is_empty():
            raise StackIsEmptyException()

        return self._values.pop()

    def peek(self):
        if self.is_empty():
            raise StackIsEmptyException()

        return self._values[-1]

    def is_empty(self):
        return len(self._values) == 0

    # für Hanoi
    def size(self):
        return len(self._values)

    def get_at(self, pos):
        return self._values[pos]


class StackIsEmptyException(Exception):
    pass


def main():
    stack = Stack()
    stack.push("first")
    stack.push("second")

    print("PEEK: " + stack.peek())
    print("POP: " + stack.pop())
    print("POP: " + stack.pop())
    print("ISEMPTY: " + str(stack.is_empty()))
    # print("POP: " + stack.pop())


if __name__ == "__main__":
    main()
