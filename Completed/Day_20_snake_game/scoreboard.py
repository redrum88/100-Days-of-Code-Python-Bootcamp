from turtle import Turtle

ALIGNMENT = "center"
MOVE = False
FONT = ("Arial", 10, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
   #     self.clear()
        self.score = 0
        with open("data.txt") as result:
            content = result.read()
            self.high_score = int(content)
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        with open("data.txt") as now:
            top_score = now.read()
        self.write(f"Score: {self.score} High Score: {top_score}", align=ALIGNMENT, move=MOVE, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            new_highscore = self.score
            with open("data.txt", mode="w") as result:
                result.write(str(new_highscore))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, move=MOVE, font=("Arial", 16, "normal"))

    def increase_score(self):
        self.score += 1

        self.update_score()