from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        # Create the paddle (Turtle object)
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(xcor, ycor)

    def move_up(self):
        # Move the paddle upward by 20 units
        self.sety(self.ycor() + 20)

    def move_down(self):
        # Move the paddle upward by -20 units
        self.sety(self.ycor() - 20)
