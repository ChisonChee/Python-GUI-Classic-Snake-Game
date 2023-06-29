from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(-80, 280)
        self.write(f"Score :", False, "center", ("Arial", 12, "normal"))
        self.setposition(40, 280)
        self.write(f"Highest Score :", False, "center", ("Arial", 12, "normal"))


def read_highest_score():
    with open("data.txt", mode="r") as datas:
        highest_score = int(datas.read())
    return highest_score


class Score(Scoreboard):
    def __init__(self):
        super().__init__()
        self.score = 0

    def write_score(self):
        self.setposition(-40, 280)
        self.write(f"{self.score}", False, "center", ("Arial", 12, "normal"))
        self.add_highest_score()
        self.setposition(100, 280)
        self.write(f"{read_highest_score()}", False, "center", ("Arial", 12, "normal"))

    def add_highest_score(self):
        if self.score > read_highest_score():
            with open("data.txt",mode="w") as data:
                data.write(f"{self.score}")

    def add_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"GAME OVER", False, "center", ("Arial", 50, "normal"))
