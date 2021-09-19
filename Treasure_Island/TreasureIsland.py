print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input('You have reached a T-junction. Type "left" or "right". \n').lower()

if direction == "left":
  sw = input('You have to cross a lake. Type "swim" to swim across or type "wait" to wait for a boat. \n').lower()
  if sw == "wait" :
    door = input('You have reached an island. There is a house with 3 doors in front of you. Choose one of the door(Type "R, Y or B") \n').upper()
    if door == "R":
      print("You're burnt by fire. Game Over!")
    elif door == "Y":
      print("Congratulations! You have found the treasure!")
    elif door == "B":
      print("You're eaten by beast. Game Over!")
    else:
      print("Game Over!")
  else:
    print("You're attacked by trout. Game Over!")
else:
  print("You fell into a hole. Game Over!")