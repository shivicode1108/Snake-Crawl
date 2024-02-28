from turtle import Screen
import time
from snake import Snake
from food import Food 
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=300, height=300)
screen.bgcolor("black")
screen.title('Snake Crawl')

snake = Snake()
food=Food()
scoreboard=Scoreboard()



screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with the food
    if snake.head.distance(food)< 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor()>298 or snake.head.xcor()<-298 or snake.head.ycor()>298 or snake.head.ycor()<-298:
        game_is_on=False
        scoreboard.game_over()
    

    #detect collision with tail
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()



screen.exitonclick()
