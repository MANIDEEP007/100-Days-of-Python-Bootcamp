from art import logo
from replit import clear
import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card():
  '''Returns Random card from cards'''
  return random.choice(cards)

def calculate_score(cards):
  '''Takes cards as input and return sum of cards'''
  if sum(cards) > 21 and 11 in cards:
      cards.append(1)
      cards.remove(11)
  if sum(cards) == 21 and len(cards) == 2:
    return 0 #Black Jack Value in Game
  return sum(cards)

def display(player_cards,computer_cards):
  '''Display Both Computer & User Cards & Scores as well'''
  print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
  print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

def compare(com_score,user_score):
  '''Compares computer & player scores & return result'''
  if com_score == user_score:
    return "You Draw"
  if com_score == 0:
    return "You lose, Opponent has blackjack"
  if user_score == 0:
    return "You Win with a Black Jack"
  if user_score > 21:
    return "You went over. You Lose"
  if com_score > 21:
    return "Opponent Went over. You win"
  if com_score > user_score:
    return "You Lose"
  if com_score < user_score:
    return "You Win"

def black_jack():
  #Print Game Logo
  print(logo)

  #Fetch Initial Cards
  player_cards  = [deal_card() for _ in range(2)]
  computer_cards = [deal_card() for _ in range(2)]

  #Variable to decide when game is completed
  game_over = False

  while not game_over:
    #Calculate Scores
    user_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {player_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    #Check whether already Black Jack or not and end the game
    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    else:
        #Ask user if he wants to deal cards
        another_card = input("Type 'y' to get another card, type 'n' to pass:")
        #If User Deal is over, its computer turn
        if another_card == "n":
          game_over = True
          while computer_score < 17 and computer_score !=0:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
        #Adding a random card to user
        else:
          player_cards.append(deal_card())
        #Calculate the scores
        user_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

  #Once Game is over, display cards, scores, result
  display(player_cards,computer_cards)
  print(compare(computer_score,user_score))

play_game = True
while play_game:
  choice = input("Do you want to play Black Jack. Type 'y' or 'n': ")
  if choice == "y":
    clear()
    black_jack()
  else:
    play_game = False
