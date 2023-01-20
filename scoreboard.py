from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(x=200, y=250)
        self.write(f"Current score: {self.score}", move=False, align='left', font=('Arial', 15, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Current score: {self.score}", move=False, align='left', font=('Arial', 15, 'normal'))
