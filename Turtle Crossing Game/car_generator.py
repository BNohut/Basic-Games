from turtle import Turtle
from random import *

COLORS = ["red", "black", "brown", "yellow", "orange", "blue", "cyan2", "purple", "pink"]

LEVEL_1 = [-140, 0, 100, 150]
LEVEL_2 = [-280, -180, -80, 0, 80, 180]
LEVEL_3 = [-280, -240, -200, -160, -120, -80, 0, 80, 120, 160, 200, 240]


class CarGenerator(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        # self.create_cars()

    def create_cars(self, level):
        for _ in range(1):
            self.add_car(level)

    def add_car(self, level):
        color = choice(COLORS)
        car = Turtle("square")
        car.shapesize(1, 2)
        car.color(color)
        car.penup()
        car.setheading(180)
        car.setposition(280, choice(level))
        self.cars.append(car)

    def cars_move(self):
        for cars in self.cars:
            cars.fd(50)

    def again(self, level):
        self.create_cars(level)
