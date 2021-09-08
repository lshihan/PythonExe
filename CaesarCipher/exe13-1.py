# from replit import clear
#HINT: You can call clear() to clear the output in the console.
import os
from art import logo1
print(logo1)

name_bid = {}
end = False

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def find_highest_bid(bidding):
    highest_bid = 0
    winner = ""
    for x in bidding:
        bid_amount = bidding[x]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = x
    print(f"The winner is {winner} and the bid is {highest_bid}")


while not end:
    name = input("What's your name?: ")
    bid = int(input("What's your bid price?:$ "))
    name_bid[name] = bid
    restart = input("Type 'Yes' if there any users to bid, if not type 'No':").lower()
    if restart == "no":
        end = True
        find_highest_bid(name_bid)
    elif restart == "yes":
        clear()