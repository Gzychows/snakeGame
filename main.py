from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

from snake import Snake

# *************************
# *****SCREEN SETTINGS*****
# *************************

# Declaring objects
screen = Screen()

# Screen size
screen.setup(width=600, height=600)

# Screen color
screen.bgcolor("black")

# Screen Title
screen.title("Snake Game")

# Turning Tracer off
screen.tracer(0)

# ************************
# *****SNAKE SETTINGS*****
# ************************

# Creating object
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listening to keyboard input
screen.listen()

# Keyboard control settings
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# ***********************
# *****GAME SETTINGS*****
# ***********************

game_is_on = True
while game_is_on:

    # Screen refresh rate settings
    screen.update()
    time.sleep(0.1)

    # Creating snake
    snake.move()

    # Detecting collision with food
    if snake.head.distance(food) < 20:
        # Moving food to new location
        food.refresh()

        # Adding new segment to the snake
        snake.extend()

        # Displaying score board
        scoreboard.increase_score()

    # Detecting collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detecting collision with tail
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# Closing screen
screen.exitonclick()
