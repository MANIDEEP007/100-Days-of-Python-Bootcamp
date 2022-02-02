#Import Turtle, Screen class from turtle Graphics module
from turtle import Turtle, Screen

#Create Turtle object
timmy = Turtle()

#Change shape of timmy from arrow to turtle
timmy.shape("turtle")

#Changing the color of the turtle - Method Calling
timmy.color("coral")

#Draw the square
for _ in range(4):
	timmy.right(90)
	timmy.forward(100)

#Create Screen object
screen_obj = Screen()

#Exit Screen or Canvas only on clicking screen
screen_obj.exitonclick()
