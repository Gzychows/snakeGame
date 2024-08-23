from turtle import Turtle
import random


# Inheriting Turtle class into Food class
class Food(Turtle):

    def __init__(self):
        super().__init__()
        # Lifting pen up
        self.penup()

        # Shape of the food
        self.shape("circle")

        # Size of the food
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)

        # Color of the food
        self.color("blue")

        # Rendering speed
        self.speed("fastest")

        # Creating new random place for food
        self.refresh()

    def refresh(self):
        # Creating random coordinates for food to appear
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)

        # Placing food to random location
        self.goto(random_x, random_y)
