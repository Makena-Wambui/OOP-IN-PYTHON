#!/usr/bin/python3

from turtle import *

t1 = Turtle()

# lets give our object properties
t1.color("red")
t1.width(5)
t1.speed()

t1.begin_fill()
for i in range(5):
    t1.fd(150)
    t1.left(144)
t1.end_fill()

done()
