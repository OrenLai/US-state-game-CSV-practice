from turtle import Turtle

FONT = ("Courier", 6, "normal")


class NameWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_name(self, coordinate, name):
        self.goto(coordinate)
        self.write(name, align="center", font=FONT)
