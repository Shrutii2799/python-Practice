import random
import turtle as t
from turtle import Screen

tim= t.Turtle()
t.colormode(255)

def random_colour():
    r=  random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour  =(r,g,b )
    return random_colour

tim.color(random_colour())


tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range (int(360/size_of_gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)
draw_spirograph(2)









screen =t.Screen()
screen.exitonclick()