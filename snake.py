from turtle import Turtle



class snake():
    def __init__(self):
        self.turtle_=[]
        self.pos=[(-40,0),(-20,0),(0,0)]

        self.game_on()
        self.move()

    def game_on(self):
        for i in range(len(self.pos)):
            hi=Turtle()

            hi.shape("square")
            hi.color("white")
            hi.penup()
            hi.goto(self.pos[i])
            self.turtle_.append(hi)
            
            self.head=self.turtle_[-1]
            self.turtle_[-1].color("#ECEBEB")

    def move(self):
        for i in range(len(self.turtle_)-1):
            self.turtle_[i].goto(self.turtle_[i+1].pos())
        self.head.forward(10)


    


    def exend(self):
        mo=Turtle()
        mo.shape("square")
        mo.color("white")
        mo.penup()
        mo.goto(self.turtle_[0].pos())
        self.turtle_.insert(0,mo) 

    def Up(self):
        self.head.setheading(90)

    def Down(self):
        self.head.setheading(270)

    def Left(self):
        self.head.setheading(180)

    def Right(self):
        self.head.setheading(0)
        




