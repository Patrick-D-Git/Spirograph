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
    """ Returns a tuple with three random generated numbers"""
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    color = (r, g, b)
    return color


def spirograph(gap):
    """Creates the Spirograph"""
    for _ in range(int(360 / gap)):
        angle = tim.heading() + gap
        tim.pencolor(random_color())
        tim.setheading(angle)
        tim.circle(100)


spirograph(5)  # calls the spirograph function where you can input a gap of your choice.

screen.exitonclick()
