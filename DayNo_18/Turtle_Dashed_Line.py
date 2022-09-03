#Import Turtle
from turtle import Turtle,Screen

#Create a Turtle Object
tur = Turtle()

#Draw a Dashed Line
for _ in range(20):
  tur.forward(10)
  tur.penup()
  tur.forward(10)
  tur.pendown()

#Create Screen object
screen_obj = Screen()

#Exit Screen or Canvas only on clicking screen
screen_obj.exitonclick()
