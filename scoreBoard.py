from turtle import Turtle
FONT=('Arial', 24, 'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,270)
        self.color("white")
        self.write(f"Score: {self.score}",align="center",font=FONT)
        self.penup()
        self.hideturtle()

    def increaseScore(self):
        self.clear()
        self.score+=1
        self.write(f"Score: {self.score}", align="center",font=FONT)

    def gameOver(self):
        self.goto(0,0)
        self.write(f"Game Over!", align="center",font=FONT)
