# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import turtle


def draw_snowflake(turtle, length, depth):
    if depth == 0:
        return

    for _ in range(6):
        turtle.right(60)
        turtle.forward(length)

        # rekursiver Abstieg
        draw_snowflake(turtle, length // 3, depth - 1)

        turtle.back(length)


screen = turtle.Screen()
turtle.speed(10)
draw_snowflake(turtle, 240, 5)
screen.exitonclick()
