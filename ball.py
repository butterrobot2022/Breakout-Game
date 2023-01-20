from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(x=0, y=0)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() - self.y_move
        self.goto(new_x, new_y)

    def reverse_y(self):
        self.y_move *= -1

    def game_over(self):
        self.clear()
        self.goto(x=-75, y=0)
        self.write("Game over!", move=False, align='left', font=('Arial', 25, 'normal'))

    def reverse_x(self):
        self.x_move *= -1

