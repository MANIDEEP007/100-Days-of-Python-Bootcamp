'''
write a program which will select a random name from a list of names. 
The person selected will have to pay for everybody's food bill. 
'''
# Split string method
names_string = input("Give me everybody's names, separated by a comma.\n ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Get the random index from List using random module
import random
names_index = random.randint(0,len(names)-1) 

#Print the name who's going to pay bill using random index
print("{} is going to buy the meal today!".format(names[names_index]))
