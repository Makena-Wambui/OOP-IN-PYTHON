#!/usr/bin/python3
"""
This module uses the turtle module to illustrate object properties and methods.
"""

# Import everything from the turtle module
from turtle import *

# create two objects using the class Turtle from turtle module
t1 = Turtle()
t2 = Turtle()

# lets assign the color property to each object
t1.color("purple")
t2.color("orange")

# link two methods to each object
t1.forward(200)
t1.right(90)

t2.left(90)
t2.forward(200)
# done allows the drawing to stay on the screen once it is completed
done()
