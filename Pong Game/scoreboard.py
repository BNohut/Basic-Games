from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-80, 200)
        self.write(self.l_score, align="center", font=("Arial", 70, "normal"))
        self.goto(80, 200)
        self.write(self.r_score, align="center", font=("Arial", 70, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def draw_line(self):
        draw = Turtle()
        draw.color("white")
        draw.penup()
        draw.setposition(0, 300)
        draw.hideturtle()
        draw.setheading(270)
        for _ in range(6):
            draw.pendown()
            draw.fd(50)
            draw.penup()
            draw.fd(50)

