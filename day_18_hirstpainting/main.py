# import colorgram
import random
from turtle import *
from turtle import Turtle

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
# print(rgb_colors)
colormode(255)
rgb_colors = [(182, 65, 34), (213, 149, 97), (14, 24, 42), (239, 208, 94), (237, 62, 33), (157, 26, 19), (72, 29, 32), (84, 94, 115), (166, 141, 66), (67, 41, 35), (120, 32, 37), (183, 85, 94), (135, 152, 164), (49, 52, 127), (229, 175, 161), (165, 64, 70), (167, 141, 150), (98, 113, 112), (160, 168, 165), (189, 190, 196), (217, 174, 180), (15, 25, 24), (79, 70, 43), (183, 196, 189), (119, 121, 147), (248, 196, 4)]
angle = 0
directions = [0, 90, 180, 270]
tim: Turtle = Turtle()
#tim.shape("turtle")
tim.hideturtle()
tim.speed(0)
tim.penup()
def line1():
    tim.setheading(225)
    tim.forward(350)
    tim.setheading(0)

def dots():
    for _ in range(10):
        tim.dot(20, random.choice(rgb_colors)); tim.fd(50)
    tim.position()

def switch_line():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)



line1()
for _ in range(10):
    dots()
    switch_line()
tim.setheading(270)
tim.forward(550)




screen = Screen()
screen.exitonclick()