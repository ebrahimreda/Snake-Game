from turtle import Screen
from snake import snake
import time
from food import food
from scoreboard import score


window=Screen()

window.bgcolor("black")
window.setup(808,800)
window.title("snake game")
window.tracer(0)

Snake=snake()
food_=food()
Score=score()

window.listen()
window.onkey(Snake.Up,"Up")
window.onkey(Snake.Down,"Down")
window.onkey(Snake.Right,"Right")
window.onkey(Snake.Left,"Left")

game_on=True
while game_on:
    Snake.move()
    window.update()
    time.sleep(0.1)

    if Snake.head.distance(food_)<13.5:
        food_.random_food()
        Snake.exend()
        Snake.exend()
        Score.food_score()

    if Snake.head.xcor() > 400 or Snake.head.xcor() < -400 or Snake.head.ycor() > 400 or Snake.head.ycor() < -400:
        game_on = False
        Score.game_over()

    # Collision with body
    for segment in Snake.turtle_[:-1]:
        if Snake.head.distance(segment) < 9.5:
            game_on = False
            Score.game_over()
     
       

        


        
        

window.exitonclick()


