from turtle import *
import pandas

# from tkinter import *
from tkinter import messagebox

screen = Screen()
screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
states = data["state"]
list_of_states = states.to_list()

correct_count = 0
correct_states = []

while correct_count < 50:
    user_input = screen.textinput(f"{correct_count}/50 States Correct", "What's another state name?").title()
    if user_input in correct_states:
        messagebox.showinfo("Warning!", "You've already entered this state.")
    elif user_input == "Exit":
        learn_states = [state for state in list_of_states if state not in correct_states]
        dict_of_learn = {
            "State": learn_states
        }
        states_to_learn = pandas.DataFrame(dict_of_learn)
        states_to_learn.to_csv("states_to_learn.csv")
        messagebox.showinfo("Warning!", "Your 'States To Learn' File is Ready in main folder.")
        break
    else:
        if user_input in list_of_states:
            position_y = int(data[data["state"] == user_input].y)
            position_x = int(data[data["state"] == user_input].x)
            correct_count += 1
            correct_states.append(user_input)
            name = Turtle()
            name.hideturtle()
            name.penup()
            name.goto(position_x, position_y)
            name.write(f"{user_input}", font=("Arial", 8, "normal"))
        else:
            messagebox.showinfo("Warning!", "There is not any state like this.")
