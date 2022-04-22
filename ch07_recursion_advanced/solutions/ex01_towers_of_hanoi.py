# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


from ch07_recursion_advanced.solutions.ex01_tower import Tower


def solve_tower_of_hanoi(n):
    print("Tower Of Hanoi", n)
    move_tower(n, 'A', 'B', 'C')


def move_tower(n, source, helper, destination):
    if n == 1:
        print(source + " -> " + destination)
    else:
        # bewege alle bis auf letzte Scheibe von Quelle auf Hilfsstab
        # Ziel wird so zum neuen Hilfsstab
        move_tower(n - 1, source, destination, helper)
        # bewege die größte Scheibe von Quelle zum Ziel
        print(source + " -> " + destination)
        # moveTower(1, source, helper, destination); // unverständlicher
        # bewege um eins reduzierten Turm von Hilfsstab auf Ziel
        move_tower(n - 1, helper, source, destination)


def solve_tower_of_hanoi_v2(n):
    print("Tower Of Hanoi", n)

    source = Tower("A")
    helper = Tower("B")
    destination = Tower("C")

    # Achtung umgekehrte Reihenfolge: größte Scheibe zuerst
    for i in range(n, 0, -1):
        source.push(i)

    action = lambda: print_towers(n + 1, source, helper, destination)
    action()

    move_tower_v2(n, source, helper, destination, action)


def move_tower_v2(n, source, helper, destination, action):
    if n == 1:
        elem_to_move = source.pop()
        destination.push(elem_to_move)

        print("Moving slice:", elem_to_move, ":", source, "->", destination)
        action()

    else:
        move_tower_v2(n - 1, source, destination, helper, action)
        move_tower_v2(1, source, helper, destination, action)
        move_tower_v2(n - 1, helper, source, destination, action)


def print_towers(max_height, source, helper, destination):
    tower1 = source.print_tower(max_height)
    tower2 = helper.print_tower(max_height)
    tower3 = destination.print_tower(max_height)

    #for i in range(len(tower1)):
    #    print(tower1[i] + "   " + tower2[i] + "   " + tower3[i])
    for (a,b,c) in zip(tower1, tower2, tower3):
        print(a + "   " + b + "   " + c)


def main():
    solve_tower_of_hanoi(3)

    solve_tower_of_hanoi_v2(2)


if __name__ == "__main__":
    main()
