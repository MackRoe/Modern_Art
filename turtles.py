from turtle import *
from random import *
import turtle


def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color(red, green, blue)


def random_place():
    penup()
    x = randint(-100, 100)
    y = randint(-100, 100)
    goto(x, y)
    pendown()


def random_heading():
    setheading(randint(0, 360))


screen = turtle.Screen()
screen.setup(720, 360)
screen.colormode(255)
shape('turtle')
for i in range(30):
    random_color()
    random_heading()
    random_place()
    stamp()


if __name__ == '__main__':
    app.run(debug=True)
