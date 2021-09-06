from turtle import Turtle

STARTING_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for coordinate in STARTING_COORDINATES:
            self.add_square(coordinate)

    def add_square(self, coordinate):
        square = Turtle(shape="square")
        square.penup()
        square.color("white")
        square.goto(coordinate)
        self.snake.append(square)

    def grow(self):
        self.add_square(self.snake[-1].position())

    def move(self):
        for square in range(len(self.snake) - 1, 0, -1):
            x_coordinate = self.snake[square - 1].xcor()
            y_coordinate = self.snake[square - 1].ycor()
            self.snake[square].goto(x_coordinate, y_coordinate)
        self.snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset_snake(self):
        for square in self.snake:
            square.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
