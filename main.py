from turtle import Screen

from ball import Ball
from paddle import Paddle

import time

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)  # Turn off the screen animation

l_paddle = Paddle(xcor=350, ycor=0)
r_paddle = Paddle(xcor=-350, ycor=0)
ball = Ball()

# Listen for keyboard input and bind keys
screen.listen()

# Bind the arrow keys to the move_up and move_down functions
screen.onkeypress(l_paddle.move_up, "Up")
screen.onkeypress(l_paddle.move_down, "Down")
screen.onkeypress(r_paddle.move_up, "w")
screen.onkeypress(r_paddle.move_down, "s")

game_is_on = True

# while loop to continuously updating the screen
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

# Exit on click
screen.exitonclick()
