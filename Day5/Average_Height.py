'''
Input: Heights of Students seperated by space
Output: Calculate Average height without using len() and sum()
'''
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
#Init variables for calculating sum of heights & number of students
no_of_stu = 0
height_sum = 0

#Iterate over the student_heights to find sum of heights & number of students
for each in student_heights:
  no_of_stu += 1
  height_sum += each

#Calculate Average height
avg_height = height_sum / no_of_stu

#Print Average Height round up to nearest whole number
print(round(avg_height))
