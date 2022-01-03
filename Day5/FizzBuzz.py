'''
You are going to write a program that automatically prints the solution to the FizzBuzz game.

    Your program should print each number from 1 to 100 in turn.

    When the number is divisible by 3 then instead of printing the number it should print "Fizz".

    `When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 
    `When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 

      `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`
'''
#Itearate over numbers 1-100
for num in range(1,101):
  #If num is divisible by 3 and 5, then print FizzBuzz
  if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
  #If num  is divisible by only 3, then print Fizz
  elif num % 3 == 0:
    print("Fizz")
  #If num is divisible by only 5, then print Buzz
  elif num % 5 == 0:
    print("Buzz")
  #If none of the above conditions match, print num
  else:
    print(num)
