from turtle import Turtle

# Text constant variables
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        # Score variable
        self.score = 0

        # Raising the pen
        self.penup()

        # Setting shape
        self.shape(name="blank")

        # Text Color
        self.color("white")

        # Text position
        self.goto(0, 260)

        # Displaying score
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        # Text position
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
