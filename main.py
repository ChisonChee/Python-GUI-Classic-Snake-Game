from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard, Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
score = Score()

snake.segment_list[0].reset()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.listen()
game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    score.write_score()
    if snake.segment_list[0].distance(food.position()) <= 15:
        snake.extend()
        food.refresh()
        score.add_score()
    if snake.segment_list[0].xcor() > 280 or snake.segment_list[0].xcor() < -280 or snake.segment_list[
        0].ycor() < -280 or snake.segment_list[0].ycor() > 280:
        game_is_on = False
        score.game_over()
    for segment in snake.segment_list[1:]:
        if snake.segment_list[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
