#Function only in REPLIT Site for clear screen
from replit import clear
#HINT: You can call clear() to clear the output in the console.
from Auction_Art import logo

#Print ASCII Art of Gavel
print(logo)

#Empty Dictionary to Store Bidder Name & Bid Value
bidders = {}

#Initial Choice to Yes
choice = "yes"
 
#While bidders are there, take their input
while choice == "yes":
  #Take Input name, amount and store in bidders dictionary
  bidder_name = input("What is your name?: ")
  bid_amount = int(input("What is your bid?: $"))
  bidders[bidder_name] = bid_amount
  choice = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  max_bidder =  (None,None)
  if choice == "no":
    for each_bidder in bidders:
      if max_bidder[1] is None or max_bidder[1] < bidders[each_bidder]:
        max_bidder = (each_bidder,bidders[each_bidder])
    print(f"The winner is {max_bidder[0]} with a bid of ${max_bidder[1]}")
  else:
    clear()
