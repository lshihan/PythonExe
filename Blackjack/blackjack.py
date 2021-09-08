from blackjack_art import logo
import os
import random

def clear():
  if os.name == "nt":
    _ = os.system('cls')

def calculate_score(card):
  if sum(card) == 21 and len(card) == 2:
    return 0

  if 11 in card and sum(card) > 21:
    card.remove(11)
    card.append(1)
  return sum(card)

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def compare(user_score,comp_score):
  if user_score >21 and comp_score>21:
    return "You went over. You lose!"
  
  if user_score == comp_score:
    return "Draw!"
  elif user_score == 0:
    return "You win with a Blackjack!"
  elif comp_score == 0:
    return "Computer wins with a Blackjack!"
  elif user_score >21:
    return "You went over. You lose!"
  elif comp_score >21:
    return "Computer went over. You win!"
  elif user_score > comp_score:
    return "You win!"
  else:
    return "You lose!"

def play_game():

  print(logo)

  user_cards = []
  comp_cards = []
  is_game_over = False

  for c in range(2):
    user_cards.append(deal_card())
    comp_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    comp_score = calculate_score(comp_cards)
    print(f"  User's card = {user_cards}, current score = {user_score}")
    print(f"  Computer's first card = {comp_cards[0]}")

    if user_score == 0 or comp_score == 0 or user_score > 21:
      is_game_over = True
    else:
      res = input("Type 'y' to draw a new card, 'n' to end your turn.\n")
      if res == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while comp_score != 0 and comp_score < 17:
    comp_cards.append(deal_card())
    comp_score = calculate_score(comp_cards)

  print(f"  Your final hand = {user_cards}, final score ={user_score}")
  print(f"  Computer's final hand = {comp_cards}, final score ={comp_score}")
  print(compare(user_score,comp_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n'\n") == 'y':
  clear()
  play_game()

