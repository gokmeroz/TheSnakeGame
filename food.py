import random
from turtle import Turtle
import random
class Food(Turtle):

   def __init__(self):
       super().__init__()
       self.shape("circle")
       self.penup()
       self.shapesize(0.5,0.5)
       self.color("green")
       self.speed("fastest")
       self.refreshLocationOfFood()

   def refreshLocationOfFood(self):
       randomX = random.randint(-280, 280)
       randomY = random.randint(-280, 280)
       self.goto(randomX, randomY)