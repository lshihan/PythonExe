import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list1 = [rock, paper, scissors]
c_choice = random.choice(list1)
p_choice = input('Welcome to Rock, Scissors, Paper Game. Type "Rock", "Scissors" or "Paper" to start the game!').lower()

if p_choice == "rock":
  if c_choice == rock:
    print("Your choice is\n" + rock)
    print("Computer choice is\n" + rock)
    print("Tie")
  elif c_choice == paper:
    print("Your choice is\n" + rock)
    print("Computer choice is\n" + paper)
    print("You lose!")
  else:
    print("Your choice is\n" + rock)
    print("Computer choice is\n" + scissors)
    print("You win!")
elif p_choice == "paper":
  if c_choice == paper:
    print("Your choice is\n" + paper)
    print("Computer choice is\n" + paper)
    print("Tie")
  elif c_choice == scissors:
    print("Your choice is\n" + paper)
    print("Computer choice is\n" + scissors)
    print("You lose!")
  else:
    print("Your choice is\n" + paper)
    print("Computer choice is\n" + rock)
    print("You win!")
elif p_choice == "scissors":
  if c_choice == scissors:
    print("Your choice is\n" + scissors)
    print("Computer choice is\n" + scissors)
    print("Tie")
  elif c_choice == rock:
    print("Your choice is\n" + scissors)
    print("Computer choice is\n" + rock)
    print("You lose!")
  else:
    print("Your choice is\n" + scissors)
    print("Computer choice is\n" + paper)
    print("You win!")
else:
    print("Invalid Input!")