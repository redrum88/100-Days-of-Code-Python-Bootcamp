import random
import turtle
from turtle import Turtle, Screen

# Adding screen
is_race_on = False

# Adding turtle

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

pointer = Turtle()
pointer.penup()
pointer.goto(x=230, y=-200)
pointer.setheading(90)
pointer.pendown()
pointer.forward(350)
pointer.isvisible()



is_race_on = True
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_axis = [-100, -60, -20, 20, 60, 100]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-225, y=y_axis[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                is_race_on = False
                print(f"You win! Turtle '{user_bet.capitalize()}' won race!")
            else:
                is_race_on = False
                print(f"You lost! Turtle '{winning_color.capitalize()}' was faster!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()