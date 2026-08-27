
import turtle as t
from turtle import Screen

tim=t.Turtle()



for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

# tim.shape("turtle")
# tim.color("red")
# screen =Screen()
# screen.exitonclick()
# for draw in range (11):
#
#
#     tim.forward(11)
#         if draw%2== 0:
#             print("_")
#         else:
#             print(" ")
#
screen =Screen()
screen.exitonclick()