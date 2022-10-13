import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from turtle import Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car = CarManager()

line1 = Turtle()
line1.penup()
line1.goto(x=300, y=290)
line1.pendown()
line1.goto(x=-300, y=290)
line1.hideturtle()

screen.listen()
screen.onkeypress(player.up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.recycle_car()
    car.move_cars()
    if player.win_condition():
        scoreboard.add_score()
        scoreboard.update_scoreboard()
        car.increase_speed()
    if car.lose_condition(player.ycor()):
        game_is_on = False
        scoreboard.game_over()
screen.exitonclick()
