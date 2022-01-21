from art import *
from game_data import data
from replit import clear
import random

#Get the random record from the data
def get_row(current):
  if current == None:
    return random.choice(data)
  row = random.choice(data)
  while current['name'] == row['name']:
    row  = random.choice(data)
  return row

#Compare the given items and return which is bigger "A" or "B"
def compare(first,second):
  if first['follower_count'] > second['follower_count']:
    return "A"
  else:
    return "B"

#Flag to exit game
exit_game = False

#Initializing first item and score
first_item = get_row(None)
score = 0

#While Exit flag is not True
while not exit_game:
  #Display Logo
  print(logo)
  
  #Display Second item
  second_item = get_row(first_item)

  #Display progress
  if score !=0:
    print(f"You're right! Current score: {score}.")
  #Display items to be compared
  print(f"Compare A: {first_item['name']}, a {first_item['description']}, from {first_item['country']}.")
  print(vs)
  print(f"Against B: {second_item['name']}, a {second_item['description']}, from {second_item['country']}.")
  #Get the user guess
  guess = input("Who has more followers? Type 'A' or 'B': ").upper()
  
  #Compare user guess & answer - If right proceed to next
  if compare(first_item,second_item) == guess:
    score +=1
    first_item = second_item
    second_item = get_row(first_item)
    clear()
  #If user guess is wrong, clear screen, display logo and final score
  else:
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    exit_game = True
