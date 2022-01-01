'''
write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x
'''
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#Initialize the highest score to None
max_score =  None

#Iterate over student_scores list
for score in student_scores:
  #Update Maximum Height when its None or less than current height
  if max_score is None or score > max_score:
    max_score = score

#Print Maximum Score
print("The highest score in the class is: {}".format(max_score))
