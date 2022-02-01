from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#Initialize empty list question_bank
question_bank = []

#Iterate over the list of dictionaries having question text and answer
for each_dict in question_data:
  #Get the text and answer from each dictionary
  text = each_dict["text"]
  answer = each_dict["answer"]
  #Create Question object using text,answer and add to question_bank
  question_bank.append(Question(text,answer))

#Create Quiz Brain object using question bank
quiz_brain = QuizBrain(question_bank)

#Get the question using quiz brain object
while quiz_brain.still_has_questions():
  quiz_brain.next_question()

#Once Quiz is completed, print final score
print("You've completed the quiz")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")
