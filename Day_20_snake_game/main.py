from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
SNAKE_SPEED = 0.2
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake v0.1 by REDRUM")
screen.tracer(0)
snake = Snake()
food =  Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

power = True
while power:
    screen.update()
    time.sleep(SNAKE_SPEED)
    snake.move()

    # TODO Detect collision with food
    if snake.head.distance(food) < 13:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # TODO Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    #    power = False
        scoreboard.reset()
        snake.reset()

    # TODO Detect collision with tail
    #if head collides with any segments in the tail then trigger game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
    #        power = False
            scoreboard.reset()
            snake.reset()






screen.exitonclick()