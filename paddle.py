from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(x=0, y=-200)
        self.x_move = 25
        self.y_move = 25

    def move_right(self):
        new_x = self.xcor() + self.x_move
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - self.x_move
        self.goto(new_x, self.ycor())
