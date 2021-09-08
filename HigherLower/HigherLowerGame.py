from art import logo, vs
from gamedata import data
import random
import os

#Clear Function
def clear():
    if os.name == "nt":
        _ = os.system('cls')

def format_data(acc):
#Format the account data into printable format
    acc_name = acc["name"]
    acc_desc = acc["description"]
    acc_country = acc["country"]
    return f"{acc_name}, a {acc_desc} from {acc_country}"

def check_ans(guess,a_follower,b_follower):
## Use if statement to check if user is correct
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"

#Display art
print(logo)
score = 0
should_continue = True
b = random.choice(data)

# Make the game repeatable
while should_continue:

    #Randomly select account from data
    # Make Position B account to Position A at the next round
    a = b
    b = random.choice(data)
    if a == b:
        b = random.choice(data)

    print(f"Compare A = {format_data(a)}")
    print(vs)
    print(f"Against B = {format_data(b)}")

    #Ask user for a guess
    guess = input("Who has more followers on Instagram? A or B\n").lower()

    # Check if user is correct
    ## Get followers count of each account
    a_follower_count = a["follower_count"]
    b_follower_count = b["follower_count"]
    is_correct = check_ans(guess,a_follower_count,b_follower_count)
    
    # Clear score between rounds
    clear()
    print(logo)

    # Give feedback to user
    if is_correct:
        score += 1
        print(f"You're right! Current Score: {score}")
        
    else:
        should_continue = False
        print(f"Sorry, you're wrong! Final Score : {score}")
        






