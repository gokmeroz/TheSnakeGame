import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("The snake game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreBoard=ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
gameIsOn=True
while gameIsOn:
    screen.update()
    time.sleep(.1)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        snake.extend()
        scoreBoard.increaseScore()
        food.refreshLocationOfFood()
    if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()>280 or snake.segments[0].ycor()<-280:
        gameIsOn=False
        scoreBoard.gameOver()
    for segment in snake.segments:

        if segment==snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment)<1:
            scoreBoard.gameOver()
            gameIsOn=False
screen.exitonclick()

