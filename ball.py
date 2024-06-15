from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x_move = -10
        self.y_move = -10
        self.setheading(125)
        self.speed('fastest')

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.x_move *= -1

    def bounce_paddle(self):
        self.y_move *= -1
