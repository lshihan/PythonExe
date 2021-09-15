from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.",prompt="Which turtle will win the race?(red/orange/yellow/green/blue/purple)\nEnter the colour: ").lower()
color = ["red","orange","yellow","green","blue","purple"]
y_position = [-70,-40,-10,20,50,80]
all_t = []

for x in range(0,6):
    new_t = Turtle(shape="turtle")
    new_t.color(color[x])
    new_t.penup()
    new_t.goto(x=-230,y=y_position[x])
    all_t.append(new_t)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_t:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You've lost! The {winning_color} is winner!")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()