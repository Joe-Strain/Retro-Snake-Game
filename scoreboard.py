from turtle import Turtle
ALIGNMENT = "center"
SCORE_FONT = ("Courier", 15, "bold")
GAMEOVER_FONT = ("Courier", 25, "bold")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(-20, 260)
        self.pencolor("white")
        self.score = 0
        with open("data.txt", mode="r") as file:
             self.high_score = file.read()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} - High Score: {self.high_score}", align=ALIGNMENT, font=SCORE_FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.penup()
    #     self.goto(0, 0)
    #     self.pendown()
    #     self.pencolor("red")
    #     self.write("GAME OVER", align=ALIGNMENT, font=GAMEOVER_FONT)

    def increase_score(self):
        self.score +=1
        self.update_scoreboard()
