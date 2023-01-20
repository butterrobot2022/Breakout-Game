from turtle import Turtle


class Bricks(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("green")
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.goto(position)
        self.color(color)

    def remove(self):
        self.hideturtle()





