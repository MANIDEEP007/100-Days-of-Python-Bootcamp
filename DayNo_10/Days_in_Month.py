#Function to Check Leap Year
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

#Function to return number of days in a given month in given year
def days_in_month(inp_year,inp_month):
  if inp_month > 12 or inp_month < 0:
    return  "Invalid Month Received"
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if inp_month == 2 and is_leap(inp_year):
      return 29
  return month_days[inp_month - 1]
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
