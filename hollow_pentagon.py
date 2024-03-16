#!/usr/bin/python3
# Create a hoolow pentagon, each side a different color

from turtle import *

pentagon = Turtle()
colors = ["green", "red", "yellow", "blue", "purple"]
for i in range(5):
    pentagon.color(colors[i])
    pentagon.width(5)
    pentagon.fd(200)
    pentagon.left(72)

done()
