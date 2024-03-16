#!/usr/bin/python3
# Function that creates a turtle star shaped object

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

if __name__ == "__main__":
    obj = Turtle()
    star(obj, "purple", 5, 500)
