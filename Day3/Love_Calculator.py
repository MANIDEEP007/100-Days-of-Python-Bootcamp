'''
To work out the love score between two people:

    Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number
Algorithm URL: https://www.buzzfeed.com/ariannarebolini/what-are-the-chances-your-crush-is-actually-your-true-love
'''
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Convert names to upper case
first_name = name1.upper()
second_name =  name2.upper()

#Calculate number of T,R,U,E in both names
first_digit = 0
for each_let in ["T","R","U","E"]:
  first_digit += first_name.count(each_let)
  first_digit += second_name.count(each_let)

#Calculate number of L,O,V,E in both names
second_digit = 0
for each_let in ["L","O","V","E"]:
  second_digit += first_name.count(each_let)
  second_digit += second_name.count(each_let)

#Combine the digits and find score
score = int(str(first_digit) + str(second_digit))

#Print the final score and interpretations accordingly
if score < 10 or score > 90:
  print("Your score is {}, you go together like coke and mentos.".format(score))
elif score >= 40 and score <=50:
  print("Your score is {}, you are alright together.".format(score))
else:
  print("Your score is {}.".format(score))
