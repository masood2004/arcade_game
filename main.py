from turtle import Turtle, Screen

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")

# Create the paddle (Turtle object)
t1 = Turtle()
t1.color("white")
t1.shape("square")
t1.turtlesize(stretch_wid=4, stretch_len=1, outline=1)
t1.penup()
t1.goto(x=350, y=0)

# Define movement function


def move_up():
    t1.sety(t1.ycor() + 10)  # Move the paddle upward by 20 units


def move_down():
    t1.sety(t1.ycor() - 10)  # Move the paddle upward by 20 units


# Listen for keyboard input and bind keys
screen.listen()
# Bind the "Up" arrow key to the move_up function
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")

# Exit on click
screen.exitonclick()
