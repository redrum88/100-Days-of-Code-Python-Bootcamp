from turtle import Screen, Turtle
import time

segments = []
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:


    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for new in STARTING_POSITIONS:
            self.add_segment(new)


    def add_segment(self, new):
        segment = Turtle(shape="square")
        segment.speed(4)
        segment.penup()
        segment.color("white")
        segment.goto(new)
        self.segments.append(segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(600, 600)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        #Add new segment to the snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != UP and self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != DOWN and self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != LEFT and self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != RIGHT and self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
