from turtle import *

def draw_square(sz):
    "Make turtle t draw a square of sz."
    for i in range(4):
        forward(sz)
        left(90)

draw_square(100)