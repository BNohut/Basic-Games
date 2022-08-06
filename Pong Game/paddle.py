from turtle import Turtle

MOVING_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, x, y):
        """Takes coordinates for location on screen"""
        super().__init__()
        self.shape("square")
        self.penup()
        self.setposition(x, y)
        self.speed("fastest")
        self.color("white")
        self.shapesize(5, 1)

    def move_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
