import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pd.read_csv("50_states.csv")

real_state = data.state.to_list()
guessed_state = []
while len(guessed_state) <50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 states correct",prompt="What's another state name?").title()

    if answer_state == "Exit":
        
        #Own solution
        missed_state = real_state
        for i in guessed_state:
            if i in missed_state:
                missed_state.remove(i)

        # Alternative solution from course mentor
        # missed_state = []
        # for i in real_state:
        #     if i not in guessed_state:
        #         missed_state.append(i)

        df = pd.DataFrame(missed_state)
        df.to_csv("missed_state.csv") #Create new file named "missed_state.csv"

        break

    if answer_state in real_state and answer_state not in guessed_state: #After "and" conditional statement is to prevent duplicate state entry.
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state) 
        # t.write(state_data.state.item())  #if t.write(state_data.state), it will show other junk..unless using .item() method at the end

# screen.exitonclick()

## Determine x and y from the picture
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
