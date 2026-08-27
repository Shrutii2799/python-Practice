import turtle as t
from turtle import Screen
import random

tim=t.Turtle()
color=["red","blue","yellow","gold","maroon","violet","purple","navy,","skyblue","cyan","lime","green","brown"]
def draw_shape(num_sides):
    angle=360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side in range(3,11):
    tim.color(random.choice(color))
    draw_shape(shape_side)








screen =Screen()
screen.exitonclick()