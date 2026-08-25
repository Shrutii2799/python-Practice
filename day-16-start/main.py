# import another_module
#
# print(another_module.another_variable)

# import turtle
#
# timmy=turtle.Turtle()
#
# from turtle import Turtle,Screen
# #Turtle is a class
# timmy=Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
#
# my_screen =Screen()
# print(my_screen.canvheight)
# print(my_screen.exitonclick())

# import prettytable

from prettytable import PrettyTable

table=PrettyTable()
table.add_column("Pokemon name",["pikachu","squirtle"])
table.add_column("Type",["electric","water"])
table.align="l"

print(table)



