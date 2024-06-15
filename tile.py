from turtle import Turtle
from console import Console
import random

BRICKS = [
    ['red', 'tomato'],
    ['yellow', 'khaki'],
    ['blue', 'royalblue'],
    ['orangered', 'chocolate'],
    ['green', 'limegreen'],
]


class Tile(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.hideturtle()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.tiles = []
        self.make_tile()

    def make_tile(self):
        for y in range(10):
            for x in range(6):
                x_cor = (-250 + x * 100)
                y_cor = (390 - y * 20)
                self.tiles.append(Console((x_cor, y_cor), random.choice(BRICKS)))

    def delete_tile(self, tile):
        for n in self.tiles:
            if n == tile:
                tile.goto(1000, 1000)
