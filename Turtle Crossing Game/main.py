from turtle import Screen
from player import *
from car_generator import *
import time


def refresh():
    global is_continue
    # player.goto(0, -280)
    # my_screen.clear()
    is_continue = True


my_screen = Screen()
my_screen.setup(600, 600)
my_screen.title("CODING IS MAGIC")
my_screen.listen()
my_screen.tracer(0)

is_continue = True
level = LEVEL_1
while is_continue:
    player = Player()
    my_screen.listen()
    my_screen.onkey(player.move, "Up")
    cars_on_screen = CarGenerator()
    cars_on_screen.create_cars(level)
    game_is_on = True
    while game_is_on:
        my_screen.update()
        time.sleep(0.16)
        cars_on_screen.cars_move()
        cars_on_screen.again(level)
        for cars in cars_on_screen.cars:
            if player.distance(cars) < 28.7:
                game_is_on = False
                player.write("GAME OVER.", align="right", font=("Arial", 9, "normal"))
                if my_screen.textinput("Hi!", "Wanna Play? y or n: ") == "y":
                    refresh()
                    my_screen.clear()
                    my_screen.tracer(0)
                    my_screen.colormode(255)
                    level = LEVEL_1
                else:
                    is_continue = False
        if player.ycor() > 250:
            game_is_on = False
            print("You win this level.")
            level = LEVEL_2
            refresh()
            my_screen.clear()
            my_screen.tracer(0)
            my_screen.colormode(255)
            player.write("Level: 2", align="left", font=("Arial", 9, "normal"))
            # if player.ycor() > 250:
            #     game_is_on = False
            #     print("You win this level.")
            #     level = LEVEL_3
            #     my_screen.clear()
            #     my_screen.tracer(0)
            #     player.write("Level: 3")
                # if player.ycor() > 250:
                #     player.write("You Completed The Game.", align="left", font=("Arial", 9, "normal"))
                #     game_is_on = False
                #     is_continue = False






my_screen.exitonclick()
