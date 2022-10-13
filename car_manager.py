from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.segments = []
        self.speedup = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(0, 5) == 0:
            if len(self.segments) <= 15:
                new_car = Turtle("square")
                new_car.penup()
                new_car.shapesize(stretch_len=3, stretch_wid=1)
                new_car.color(random.choice(COLORS))
                new_car.setheading(180)
                new_car.goto(x=300, y=random.randint(-250, 250))
                self.segments.append(new_car)

    def recycle_car(self):
        for vehicle in self.segments:
            if vehicle.xcor() <= -300:
                vehicle.goto(x=300, y=random.randint(-250, 250))

    def move_cars(self):
        for vehicle in self.segments:
            vehicle.forward(self.speedup)

    def increase_speed(self):
        self.speedup += MOVE_INCREMENT

    def lose_condition(self, player_ycor):
        for vehicle in self.segments:
            if 30 >= vehicle.xcor() >= -30:
                if vehicle.ycor() - 15 <= player_ycor <= vehicle.ycor() + 15:
                    return True
        return False
