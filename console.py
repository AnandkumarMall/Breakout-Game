from turtle import Turtle


class Console(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.color(color[0], color[1])
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())


