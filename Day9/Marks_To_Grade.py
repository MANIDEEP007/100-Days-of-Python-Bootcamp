#Convert Scores to Grades
'''
Scoring Criteria
    Scores 91 - 100: Grade = "Outstanding"
    Scores 81 - 90: Grade = "Exceeds Expectations"
    Scores 71 - 80: Grade = "Acceptable"
    Scores 70 or lower: Grade = "Fail"
'''
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student_name in student_scores:
  score = student_scores[student_name]
  if score >=91 and score <= 100:
    student_grades[student_name] = "Outstanding"
  elif score >=81 and score <= 90:
    student_grades[student_name] = "Exceeds Expectations"
  elif score >=71 and score <= 80:
    student_grades[student_name] = "Acceptable"
  else:
    student_grades[student_name] = "Fail"
    

# 🚨 Don't change the code below 👇
print(student_grades)
