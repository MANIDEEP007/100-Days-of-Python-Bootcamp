'''
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
'''
#Write your code below this line 👇
import math
def paint_calc(width,height,cover):
  #Calculate the area of wall
  area = width * height
  #Find needed cans and round to nearest big whole number
  cans = math.ceil(area/cover)
  print(f"You'll need {cans} cans of paint.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
