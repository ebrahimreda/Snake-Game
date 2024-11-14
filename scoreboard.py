from turtle import Turtle


class score(Turtle):
    def __init__(self ):
        super().__init__()
        self.score= 0
        self.penup() 
        self.color("white")
        self.goto(0,360)
        self.hideturtle()
        self.titil()

    def titil(self):
        self.penup()
        self.write(f"Score:{self.score}",align="center",font=("arial",24,"normal"))
        
    def food_score(self):
        self.score+=1
        self.clear()
        self.titil()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Arial", 36, "normal"))