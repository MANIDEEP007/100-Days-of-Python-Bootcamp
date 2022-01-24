#Import Turtle, Screen class from turtle Graphics module
from turtle import Turtle, Screen

#Create Turtle object
timmy = Turtle()

#Change shape of timmy from arrow to turtle
timmy.shape("turtle")

#Changing the color of the turtle - Method Calling
timmy.color("coral")

#Move the turtle by 100 forward
timmy.forward(100)

#Create Screen object
screen_obj = Screen()

#Print Canvas or Screen Width & Height - Accessing Attributes
print(screen_obj.canvheight)
print(screen_obj.canvwidth)

#Exit Screen or Canvas only on clicking screen
screen_obj.exitonclick()
