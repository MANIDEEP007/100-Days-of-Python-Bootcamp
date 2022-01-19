import random
from Art import logo

#Print the logo for the game
print(logo)

#Pick the random number to be guessed by user
com_num = random.randint(1,100)

#Print Starting messages of game
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")

#Define lives for Game as 10 until the choice is hard
lives = 10

#Take use's choice of difficulty
choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

#If choice is hard, change lives to 5
if choice == "hard":
  lives = 5

#Until lives not completed
while lives:
  #Print Lives remaining
  print(f"You have {lives} attempts remaining to guess the number")
  #Ask user to guess
  guess = int(input("Make a guess: "))
  #If number is greater than guess. Print Too low
  if com_num > guess:
    print("Too low")
  #If number is less than guess. Print Too High
  elif com_num < guess:
    print("Too high")
  #If guess is correct
  elif com_num == guess:
    print(f"You got it! The answer was {guess}")
    break
  #If guess is not right, decrease lives by 1
  lives -= 1
  if lives == 0:
    print("You've run out of gueses, you lose")
  else:
    print("Guess again")
