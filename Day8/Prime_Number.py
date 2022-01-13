#Write your code below this line 👇
def prime_checker(number):
  #If number is 2, its prime
  if number == 2:
    print("It's a prime number.")
    return
  #Else check whether its is divisible
  for each_num in range(2,number//2+1):
    #If its divisible by other than 1 & itself, its not prime
    if number % each_num == 0:
      print("It's not a prime number.")
      break
  else:
    print("It's a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
