#Import Turtle
from turtle import Turtle,Screen
import random

#Create a Turtle Object
tur = Turtle()

#List of colors
colors = ["royal blue","dark green","goldenrod",
          "saddle brown","deep pink","indigo",
          "rosy brown",
          ]
#Function to draw polygon
def draw_polygon(num_sides,color):
  angle = 360 /num_sides
  tur.pencolor(color)
  for _ in range(num_sides):
    tur.forward(100)
    tur.right(angle)  

#Draw from Triangle to Decadon
for num_sides in range(3,11):
  draw_polygon(num_sides,random.choice(colors))
  

#Create Screen object
screen_obj = Screen()

#Exit Screen or Canvas only on clicking screen
screen_obj.exitonclick()
