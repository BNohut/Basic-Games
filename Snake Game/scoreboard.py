from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
            file.close()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setposition(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:   {self.score} High Score: {self.high_score}", font=('Arial', 12, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as score:
                score.write(f"{self.high_score}")
                score.close()
        self.score = 0
        self.update_scoreboard()

    def count_score(self):
        self.score += 1
        self.update_scoreboard()
