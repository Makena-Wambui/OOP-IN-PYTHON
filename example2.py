#!/usr/bin/python3
"""
Further explanation on how to use turtle module and its methods for OOP.
"""

from turtle import *

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
# Assign a color to your object, a string.

t1.color("purple")
t2.color("red")

# width of the line
# default is 1
t1.width(5)
t2.width(5)

# Assign a shape to the object
# can be an arrow, circle, square, triangle, turtle
t1.shape("turtle")
t2.shape("turtle")

# Assign a speed to the drawing itself
# Max is 10
t1.speed()
t2.speed()

# give your object motion/ action with fd or forward
# number of pixels in ()
t1.fd(500)
t2.fd(500)

# directions, left or right
# number of degrees in ()
t1.left(45)
t2.left(90)

# lift your object off the screen
t1.up()
t2.up()

# move to a new location, x y cordinates
t1.goto(30, 15)
t2.goto(20, 15)

# place object back down once it has been moved
t1.down()
t2.down()

# use circle to draw circles, takes a radius
t3.circle(100)
t3.color("red")

# fill in your drawing with color
t3.begin_fill()
t3.end_fill()

# keep the drawing displayed once completed
done()
