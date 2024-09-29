from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 300)
        self.score = 0
        self.pencolor('white')
        self.write(f"Score: {self.score}", False,'center', ('Arial', 24, 'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, 'center', ('Arial', 24, 'normal'))
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER!!! Score: {self.score}", False, 'center', ('Arial', 32, 'normal'))
