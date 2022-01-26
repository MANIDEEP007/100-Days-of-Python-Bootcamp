from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Variable to control machine on or off
is_on = True

#Create objects of coffee machine, money maker and menu
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:
  #Get the choices available as a string
  choices_available = menu.get_items()
  #Prompt the user for choice
  choice = input(f"​What would you like? ({choices_available}):").lower()
  #Get the details of the selected drink
  drink = menu.find_drink(choice)
  #If choice is report, report resources & profit
  if choice == "report":
    coffee_maker.report()
    money_machine.report()
  #If choice is off, shutdown the coffee make
  elif choice == "off":
      print("Coffee Machine is turned off")
      is_on = False
  #Check drink is available or not
  elif drink:
    #Check for resources available or not
    if coffee_maker.is_resource_sufficient(drink):
      #Check for transcation successful or not
      if money_machine.make_payment(drink.cost):
        #If transcation is successful, make coffee
        coffee_maker.make_coffee(drink)
