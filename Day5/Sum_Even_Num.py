'''
You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.
'''
#Initialize Result to 0
result = 0

#Iterate over numbers 2-100 with step as 2 and accumulate result
for even_num in range(2,101,2):
  result += even_num

#Print the result
print(result)
