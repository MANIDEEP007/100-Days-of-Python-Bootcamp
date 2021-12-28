# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#BMI = weight/(height*height)
BMI = round(float(weight)/(float(height) ** 2))
if BMI < 18.5:
  print("Your BMI is {}, you are underweight.".format(BMI))
elif BMI < 25:
  print("Your BMI is {}, you have a normal weight.".format(BMI))
elif BMI < 30:
  print("Your BMI is {}, you are slightly overweight.".format(BMI))
elif BMI  <35:
  print("Your BMI is {}, you are obese.".format(BMI))
else:
  print("Your BMI is {}, you are clinically obese.".format(BMI))
