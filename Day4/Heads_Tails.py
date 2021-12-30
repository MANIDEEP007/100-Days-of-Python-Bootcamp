#Heads & Tails Game

#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random
#Generate a Random Integer 0 or 1
flip_value = random.randint(0,1)

#Assume 0 - Tails, 1 - Heads
if flip_value == 0:
  print("Tails")
else:
  print("Heads")
