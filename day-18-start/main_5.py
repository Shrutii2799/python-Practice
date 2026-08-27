import random
import turtle as t
from turtle import Screen

tim= t.Turtle()
t.colormode(255)

def random_colour():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_colour  =(r,g,b )
    return random_colour
# color=["red","blue","yellow","gold","maroon","violet","purple","navy","skyblue","cyan","lime","green","brown"]
direction=[0,90,180,270]
tim.speed("fastest")
tim.pensize(15)

for _ in range(200):
    tim.color(random_colour())
    # tim.color(random.choice(color))
    tim.forward(30)
    tim.setheading(random.choice(direction))
































screen =Screen()
screen.exitonclick()