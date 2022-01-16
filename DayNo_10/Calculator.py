from art import logo
from replit import clear #Only Works in replit

#Arithmetic Operations for Calculator
def add(n1,n2):
  """Adds two numbers & return the result"""
  return n1 + n2

def subtract(n1,n2):
  """Subtracts second number from first number & return the result"""
  return n1 - n2

def multiply(n1,n2):
  """Multiply two numbers & return the result"""
  return n1 * n2

def divide(n1,n2):
  """Divide first number by second number & return the result"""
  return n1 / n2

#Dictionaries mapping operators & Corresponding Functions
op_dict = {
  '+' : add,
  '-' : subtract,
  '*' : multiply,
  '/' : divide,
}

def calculator():
  #Display calculator logo
  print(logo)
  #Getting First Input Number from User
  num1 = float(input("What's the first number?:"))

  #Printing the operations available
  for each_op in op_dict:
    print(each_op)

  exit_flag = False
  while not exit_flag:
    #Choose operation from user and pick number 2
    op_sym = input("Pick an operation:")
    num2 = float(input("What's the second number?:"))
    #Based on chosen symbol, calculate and display result
    answer = op_dict[op_sym](num1,num2)
    print(f"{num1} {op_sym} {num2} =  {answer}")
    #Ask user to continue calculation with result or start fresh one
    choice = input(f"Type 'y' to continue calculation with {answer} or type 'n' to start fresh calculation: ").lower()
    if choice == "y":
      num1 = answer
    else:
      exit_flag = True
      clear()
      calculator()

calculator()
