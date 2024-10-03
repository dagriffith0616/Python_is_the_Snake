from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score
import time
def draw_border():
    artist = Turtle("turtle")
    artist.speed(5)
    artist.penup()
    artist.goto(-290, 0)
    artist.pencolor('red')
    artist.setheading(90)
    artist.pendown()
    artist.goto(-290,290)
    artist.setheading(0)
    artist.goto(290,290)
    artist.setheading(270)
    artist.goto(290, -290)
    artist.setheading(180)
    artist.goto(-290, -290)
    artist.setheading(90)
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
        time.sleep(2)
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            time.sleep(1)
            score.reset()
            snake.reset()




screen.exitonclick()




