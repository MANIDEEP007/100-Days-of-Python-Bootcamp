class QuizBrain:

  """Initializes the Quiz Brain object"""
  def __init__(self,question_bank):
    self.question_number = 0
    self.question_list = question_bank
    self.score = 0

  def still_has_questions(self):
    return not self.question_number == len(self.question_list)
  
  def check_answer(self,user_answer,correct_answer):
    if user_answer == correct_answer.lower():
      print("You got it right!")
      self.score += 1
    else:
      print("That's Wrong")
    print(f"The correct answer was {correct_answer}")
    print(f"Your current score is: {self.score}/{self.question_number}\n")


  """
  Get the question at question number position
  Increment the question_nubmer
  """
  def next_question(self):
    question_text = self.question_list[self.question_number].text
    correct_answer = self.question_list[self.question_number].answer
    self.question_number += 1
    question_str =  f"Q.{self.question_number}: {question_text}(True/False)?: "
    user_answer = input(question_str).lower()
    self.check_answer(user_answer,correct_answer)
