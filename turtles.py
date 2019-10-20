from turtle import *
from random import *


def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0,255)
    color(red, green, blue)


def random_place():
    penup()
    x = randint(-100,100)
    y = randint(-100,100)
    goto(x,y)
    pendown()

shape('turtle')
random_color()
random_place()
stamp()
random_color()
random_place()
stamp()

  if __name__ == '__main__':
    app.run(debug=True)
