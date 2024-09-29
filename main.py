from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score
import time
def draw_border():
    artist = Turtle("turtle")
    artist.speed('slow')
    artist.penup()
    artist.goto(-290, 0)
    artist.pencolor('red')
    artist.pendown()
    artist.goto(-290,290)
    artist.goto(290,290)
    artist.goto(290, -290)
    artist.goto(-290, -290)
    artist.goto(-290, 0)
    artist.hideturtle()
screen = Screen()
screen.screensize(600,600)
screen.bgcolor('black')
screen.title('Snake Game')
draw_border()
time.sleep(1)
screen.tracer(0)
snake = Snake()
food = Food()


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.down, 'Down')
game_over = False
score = Score()
while not game_over:

    screen.update()
    time.sleep(.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score.game_over()
        game_over = True

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_over = True



screen.exitonclick()
