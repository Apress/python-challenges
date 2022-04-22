# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def main():
    # list as stack
    stack_of_tasks = []

    # push "tasks" to stack
    stack_of_tasks.append("Task 1")
    stack_of_tasks.append("Task 2")
    stack_of_tasks.append("Task 3")
    stack_of_tasks.append("Task 4")

    # pop "tasks" from stack
    last_tasks = stack_of_tasks.pop()
    second_last_tasks = stack_of_tasks.pop()
    print(last_tasks)
    print(second_last_tasks)

    # list as queue
    queue_of_numbers = []

    # enqueue 3 items
    queue_of_numbers.append("First")
    queue_of_numbers.append("Second")
    queue_of_numbers.append("Third")

    # dequeue until queue is empty
    while len(queue_of_numbers) > 0:
        print("Processing " + queue_of_numbers.pop(0))


if __name__ == "__main__":
    main()
