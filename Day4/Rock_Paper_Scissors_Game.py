'''
Rock Paper Scissors Game Algorithm
-----------------------------------
Rock wins over scissors (because rock smashes scissors)
Scissors wins over paper (because scissors cut paper)
Paper wins over rock (because paper covers rock)
'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
#Mapping symbols to values
sym_dict = {
              0 : rock,
              1 : paper,
              2 : scissors
            }

#Get the User's choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

#Get the computers Choice using random module
import random
comp_choice = random.randint(0,2)

#Print User & Computer Choice
print("User Choice is:")
print(sym_dict[user_choice])
print("\n\n")
print("Computer Choice is:")
print(sym_dict[comp_choice])

#Comparision & Determing the result
if user_choice > 2 or user_choice < 0:
  print("You Lose!!")
elif user_choice == comp_choice:
  print("You Draw!!")
elif user_choice == 0 and comp_choice == 2:
  print("You Win!!")
elif user_choice > comp_choice:
  print("You Win!!")
elif user_choice < comp_choice:
  print("You Lose!!")
else:
  print("You Lose!!")
