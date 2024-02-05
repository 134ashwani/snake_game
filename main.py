from turtle import Screen
from snake import Snake
import time
from food import Food
from score_Board import Scoreboard
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game.")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    # Detect collosion with food
    # here using distance method for collosion with food
    if snake.head.distance(food)< 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_Score()

    # Detect collosion with wall
 
    if snake.head.xcor() > 290 or snake.head.xcor()< -290 or snake.head.ycor() < -290 or snake.head.ycor() >290:
        scoreboard.reset()
        snake.reset()
    # Detect collosion with tail
    for segement in snake.segements[1:]:
        # above i'm using slicing metthod that helps to chek each segment expect head or 1st segment
        if segement == snake.head:
            pass
        elif snake.head.distance(segement) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()