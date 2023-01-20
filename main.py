from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from bricks import Bricks
from scoreboard import Score

screen = Screen()
screen.bgcolor("black")
screen.title("Breakout Game!")
screen.setup(width=800, height=600)
screen.tracer(0)

green_brick_list = []
red_brick_list = []
third_green_list = []
second_red_list = []
bottom_paddle = Paddle()
ball = Ball()
for i in range(-360, 341, 70):
    red_bricks = Bricks((i, 170), "red")
    red_brick_list.append(red_bricks)

for i in range(-360, 341, 70):
    second_red_bricks = Bricks((i, 110), "red")
    second_red_list.append(second_red_bricks)


for i in range(-360, 341, 70):
    bricks = Bricks((i, 200), "green")
    green_brick_list.append(bricks)

for i in range(-360, 341, 70):
    green_bricks = Bricks((i, 140), "green")
    third_green_list.append(green_bricks)
score = Score()

game_is_on = True
sleep_time = 0.1
while game_is_on:
    screen.update()
    screen.onkey(bottom_paddle.move_right, "Right")
    screen.onkey(bottom_paddle.move_left, "Left")
    sleep(sleep_time)
    screen.listen()
    ball.move()
    if ball.ycor() < -200:
        game_is_on = False
        ball.game_over()
    if ball.distance(bottom_paddle) < 50 and ball.ycor() < -160:
        ball.reverse_y()
    if ball.ycor() > 280:
        ball.reverse_y()
    if ball.xcor() > 360 or ball.xcor() < -360:
        ball.reverse_x()
    for brick in green_brick_list:
        if ball.distance(brick) < 50 and ball.ycor() > 200:
            score.increase_score()
            brick.hideturtle()
            green_brick_list.remove(brick)
            ball.reverse_y()
            sleep_time *= 0.9
    for brick in red_brick_list:
        if ball.distance(brick) < 50 and ball.ycor() > 165:
            score.increase_score()
            brick.hideturtle()
            red_brick_list.remove(brick)
            ball.reverse_y()
            sleep_time *= 0.9
    for brick in third_green_list:
        if ball.distance(brick) < 50 and ball.ycor() > 135:
            score.increase_score()
            brick.hideturtle()
            third_green_list.remove(brick)
            ball.reverse_y()
            sleep_time *= 0.9
    for brick in second_red_list:
        if ball.distance(brick) < 50 and ball.ycor() > 105:
            score.increase_score()
            brick.hideturtle()
            second_red_list.remove(brick)
            ball.reverse_y()
            sleep_time *= 0.9

screen.exitonclick()
