from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import screen as screen

# TODO Create the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong v0.1 by REDRUM")
screen.tracer()
screen.listen()
# TODO Create and move a paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(key="Up", fun=r_paddle.up)

screen.onkey(key="Down", fun=r_paddle.down)

screen.onkey(key="w", fun=l_paddle.up)

screen.onkey(key="s", fun=l_paddle.down)
power = True
while power:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
  #  print(f"Left Score: {score_left} # Right Scoore: {score_right}")
# TODO Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()

# TODO  Detect collision with paddle



# TODO Detect when paddle misses

# TODO Keep score

screen.exitonclick()