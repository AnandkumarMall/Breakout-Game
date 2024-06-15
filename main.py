import time
from turtle import Screen
from console import Console
from ball import Ball
from tile import Tile

screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor('black')
screen.title('My Breakout Game')
screen.tracer(0)
square = Console((0, -200), ['red', 'tomato'])

ball = Ball()
tile = Tile()
screen.listen()

screen.onkey(square.move_left, key='Left')
screen.onkey(square.move_right, key='Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_wall()
    if ball.distance(square) < 37:
        ball.bounce_paddle()
    for tiles in tile.tiles:
        if ball.distance(tiles) < 37:
            ball.bounce_paddle()
            tile.delete_tile(tiles)
            

screen.exitonclick()
