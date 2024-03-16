#!/usr/bin/python3
# Functions that create turtle objects

from turtle import *

def star(obj, color, width, size):
    obj.color(color)
    obj.width(width)
    
    obj.begin_fill()
    for i in range(5):
        obj.fd(size)
        obj.left(144)
    obj.end_fill()
    done()

def circle(obj1, color, width, radius):
    obj1.color(color)
    obj1.width(width)

    obj1.begin_fill()
    obj1.circle(radius)
    obj1.end_fill()

if __name__ == "__main__":
    obj = Turtle()
    obj1 = Turtle()

    circle(obj1, "blue", 3, 150)
    star(obj, "purple", 5, 500)
