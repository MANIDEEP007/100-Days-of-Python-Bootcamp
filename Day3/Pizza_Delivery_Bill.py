'''
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
'''
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Initialize bill
bill = 0

#Bill for Pizza size
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
elif size == "L":
  bill += 25

#Bill for Pepperoni based on Pizza size
if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

#Bill for Extra Cheese
if extra_cheese == "Y":
  bill += 1

#Print the total bill
print("Your final bill is: ${}.".format(bill)) 
