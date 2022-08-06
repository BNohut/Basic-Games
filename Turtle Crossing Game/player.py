from turtle import Turtle
from car_generator import *


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setposition(0, -280)
        self.setheading(90)

    def move(self):
        self.fd(35)

    def win(self):
        if self.ycor() > 150:
            return True

