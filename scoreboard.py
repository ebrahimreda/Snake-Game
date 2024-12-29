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

    def tchec_score(self):
        with open("/home/ibrahim/learning/prejcts/Snake-Game/score.txt", "w") as file_ra:
            pass
        with open("/home/ibrahim/learning/prejcts/Snake-Game/score.txt", "r") as file_r:
            file_read = file_r.read()

        if str(self.score) <= file_read:
            self.goto(0, 0)
            self.write(f"Game Over !\nthe highest score:{file_read}", align="center", font=("Arial", 36, "normal"))

        elif str(self.score) > file_read:
            with open("/home/ibrahim/learning/prejcts/Snake-Game/score.txt", "w") as file_w:
                file_w.write(str(self.score))
            self.goto(0, 0)
            self.write(f"Game Over !\nthe highest score:{self.score}", align="center", font=("Arial", 36, "normal"))
