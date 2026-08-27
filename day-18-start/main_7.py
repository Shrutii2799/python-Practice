import turtle as turtle_module
import random

turtle_module.colormode(255)

tim= turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
colors_list = [(255, 0, 0),(0, 255, 0),(255, 255, 0), (128, 0, 128), (0, 255, 255), (255, 0, 255),  (255, 20, 147),(0, 128, 0),(128, 0, 0),(0, 0, 128),(255, 215, 0),  (173, 255, 47), (255, 192, 203), (64, 224, 208),(210, 105, 30), (255, 105, 180),(184, 134, 11),(240, 230, 140),(127, 255, 212),(255, 99, 71)]

tim.setheading(225)
tim.forward(350)
tim.setheading(0)

number_of_dots=100
for dot_count in range(1,number_of_dots+1):
    tim.dot(20, random.choice(colors_list))
    tim.forward(50)

    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

















screen=turtle_module.Screen()
screen.exitonclick()




























