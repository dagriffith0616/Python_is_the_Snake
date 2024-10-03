from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 300)
        self.score = 0
        self.high_score = 0
        self.pencolor('white')
        self.write(f"Score: {self.score}", False,'center', ('Arial', 24, 'normal'))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, 'center', ('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

