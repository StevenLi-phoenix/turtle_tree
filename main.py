import threading
import time
import turtle
import random


class nodes:
    def __init__(self, reg, turnanle, fddistance, leftright, position, heading):
        global acc, max_reg
        if reg > 0:
            acc += 1
            t = turtle.Turtle()
            t.hideturtle()
            t.speed(0)
            t.penup()
            t.setposition(position)
            t.setheading(heading)
            t.pendown()
            val = 0
            t.color((val,val,val))
            if leftright:
                t.left(turnanle)
            else:
                t.right(turnanle)
            t.forward(fddistance)
            nodes(reg - 1, turnanle, reg * 4, True, t.position(), t.heading())
            nodes(reg - 1, turnanle, reg * 4, False, t.position(), t.heading())
        else:

            if acc % 2 ** 5 == 0:
                turtle.update()


if __name__ == '__main__':
    turtle.tracer(0, 0)
    acc = 0
    max_reg = 14
    nodes(14, 20, 14 * 4, True, (0, -200), 90 - 20)
    print("DONE")
    while True:
        turtle.update()
