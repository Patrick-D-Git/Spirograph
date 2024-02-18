import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim = Turtle()
screen = Screen()

tim.shape("arrow")
tim.speed(0)
tim.circle(100)


def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    rgb = (r, g, b)
    return rgb


angle = 0
make_circle = True

while make_circle:

    if angle >= 360:
        make_circle = False

    else:
        tim.pencolor(random_color())
        tim.setheading(angle)
        tim.circle(100)
        angle += 2
        print(angle)


screen.exitonclick()
