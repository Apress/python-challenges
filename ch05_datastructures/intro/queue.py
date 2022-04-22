# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


class Queue:
    def __init__(self):
        self.values = []

    def enqueue(self, elem):
        self.values.append(elem)

    def dequeue(self):
        if self.is_empty():
            raise QueueIsEmptyException()

        return self.values.pop(0)

    def peek(self):
        if self.is_empty():
            raise QueueIsEmptyException()

        return self.values[0]

    def is_empty(self):
        return len(self.values) == 0

    # Kompatibilität (Java-Version)
    def offer(self, elem):
        self.values.append(elem)


class QueueIsEmptyException(Exception):
    pass


def main():
    waiting_persons = Queue()

    waiting_persons.enqueue("Marcello")
    waiting_persons.enqueue("Michael")
    waiting_persons.enqueue("Karthi")

    while not waiting_persons.is_empty():
        if waiting_persons.peek() == "Michael":
            # reprocess at the end
            waiting_persons.enqueue("Michael again")
            waiting_persons.enqueue("Last Man")

        next_person = waiting_persons.dequeue()
        print("Processing " + next_person)


if __name__ == "__main__":
    main()
