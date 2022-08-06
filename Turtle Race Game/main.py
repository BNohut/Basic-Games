from turtle import *
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-50, -20, 10, 40, 70, 100]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet in colors:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_bet.lower():
                print(f"Congrats! {turtle.pencolor().title()} Turtle Is The Winner!")
            else:
                print(f"Sorry! {user_bet.title()} Turtle Lose! {turtle.pencolor().title()} Is The Winner!")
        else:
            moves = random.randint(0, 10)
            turtle.fd(moves)
