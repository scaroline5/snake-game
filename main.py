from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
#scoreboard.write(arg=scoreboard.display_text, align=scoreboard.text_alignment, font=scoreboard.font)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

# Move the snake
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision of the snake with the food
    if snake.head.distance(food) < 15:
        food.set_location()
        snake.grow()
        scoreboard.update_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.reset_snake()

    # Detect collision of the snake head with the tail
    for square in snake.snake[1:]:
        if snake.head.distance(square) < 10:
            scoreboard.reset_score()
            snake.reset_snake()

screen.exitonclick()
