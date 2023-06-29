from turtle import Turtle
SEGMENT_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segment_list = []
        self.create_snake()

    def create_snake(self):
        for position in SEGMENT_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segment_list.append(segment)

    def extend(self):
        self.add_segment(self.segment_list[-1].position())

    def move(self):
        import time
        for segment in range(len(self.segment_list) - 1, 0, -1):
            xcor = self.segment_list[segment - 1].xcor()
            ycor = self.segment_list[segment - 1].ycor()
            self.segment_list[segment].setposition(xcor, ycor)
            time.sleep(0.05)
        self.segment_list[0].fd(MOVE_DISTANCE)

    def up(self):
        if self.segment_list[0].heading() != 270:
            self.segment_list[0].seth(90)
            self.segment_list[0].fd(MOVE_DISTANCE)

    def down(self):
        if self.segment_list[0].heading() != 90:
            self.segment_list[0].seth(270)

    def left(self):
        if self.segment_list[0].heading() != 0:
            self.segment_list[0].seth(180)

    def right(self):
        if self.segment_list[0].heading() != 180:
            self.segment_list[0].seth(0)
