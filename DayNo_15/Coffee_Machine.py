#Coffee Menu & Requirements
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

#Resources of Coffee Machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#Dictionary to hold types of coins and their values
coins_dict = {
    "quarters" : 0.25,
    "dimes" : 0.10,
    "nickles" : 0.05,
    "pennies" : 0.01,
}

#Initialize profit of machine to zero
resources["money"] = 0

def money_check(choice,money_dict):
  """
  Check money and if sufficient return change, else None
  """
  needed_money = MENU[choice]["cost"]
  got_money = 0
  for key in money_dict:
      got_money += (coins_dict[key] * money_dict[key])
  #If enough money is received, then calculate & return the change. Also, decrements the resources needed to make coffee from resources
  if needed_money < got_money:
    #Add the bill received as profit to coffee machine
    resources["money"] += needed_money
    for key in MENU[choice]["ingredients"]:
      resources[key] -= MENU[choice]["ingredients"][key]
    #Round change to 2 places while returning
    return  round(got_money - needed_money,2)


def print_report():
  """
  Prints the resources of the coffee machine & profit acquired
  """
  print(f"Water: {resources['water']}ml")
  print(f"Milk: {resources['milk']}ml")
  print(f"Coffee: {resources['coffee']}g")
  print(f"Money: ${resources['money']}")

def check_resources(coffee_choice):
  """
  Check if resources available for making selected coffee
  """
  for key in MENU[coffee_choice]["ingredients"]:
    if MENU[coffee_choice]["ingredients"][key] > resources[key]:
      print(f"Sorry there is not enough {key}.")
      return False
  return True

def coffee_machine():
  while True:
    #Ask for the coffee choice
    choice = input("​What would you like? (espresso/latte/cappuccino):").lower()
    #If choice is report, print the resources available & profit acquired
    if choice == "report":
      print_report()
    #If choice is off, shutdown the coffee machine
    elif choice == "off":
      print("Coffee Machine is turned off")
      return
    #If coffee choice is valid
    elif choice in MENU.keys():
      #Check for resources availability
      if check_resources(choice):
        coins_inp = {}
        #Get the coins input from users
        print("Please insert coins.")
        coins_inp["quarters"] = float(input("how many quarters?: "))
        coins_inp["dimes"] = float(input("how many dimes?: "))
        coins_inp["nickles"] = float(input("how many nickels?: "))
        coins_inp["pennies"] = float(input("how many pennies?: "))
        result = money_check(choice,coins_inp)
        #If money is not sufficient, refund it
        if result == None:
          print("Sorry that's not enough money. Money refunded.")
        #If money is sufficient, return the change and deliver coffee
        else:
          if result != 0.0:
            print(f"Here is ${result} in change.")
          print(f"Here is your f{choice} ☕️. Enjoy!")

coffee_machine()
