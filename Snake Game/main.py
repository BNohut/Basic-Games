import time
from turtle import *
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

SCORE = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        scoreboard.count_score()

    current_x = snake.head.xcor()
    current_y = snake.head.ycor()
    if current_x > 290 or current_x < -290 or current_y > 290 or current_y < -290:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
