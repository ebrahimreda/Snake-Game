from turtle import Turtle
import random

class food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(0.5,0.5)
        self.penup()
        
        self.random_food()


    def random_food(self):
        self.cor_y=random.randint(-380,380)
        self.cor_x=random.randint(-380,380)
        
        self.goto(self.cor_x,self.cor_y)
       




