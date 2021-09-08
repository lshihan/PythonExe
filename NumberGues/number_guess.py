#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import os
from random import randint
from number_guessart import logo
user_attempt_easy = 10
user_attempt_hard = 5


def clear():
    if os.name == "nt":
        _ = os.system('cls')

def check_attempt():
    diff = input("Please select your game difficulty. Easy/Hard\n").lower()
    if diff == "hard":
        return user_attempt_hard
    elif diff == "easy":
        return user_attempt_easy
    else:
        return "Please type correctly!"

def check_guess(guess, answer, turns):
    if guess > answer:
        print(" Too high")
        return turns -1
    elif guess < answer:
        print(" Too low")
        return turns -1
    else:
        print(f"You got it! The answer was {answer}.")

def game():
    print(logo)
    print("Welcome to GuessTheNumber!")
    answer = randint(1,100)

    turns = check_attempt()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number!")
        guess = int(input("Guess a number between 1 to 100:\n   "))
        turns = check_guess(guess, answer,turns)
        if turns == 0:
            print("You have run out of guesses!")
            return
        elif guess != answer:
            print("Guess again.")

game()


    