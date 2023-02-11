import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shape("square")
        new_car.turtlesize(stretch_wid=1, stretch_len=2)
        new_car.goto(300, random.randint(-250, 250))
        self.car_list.append(new_car)

    def car_move(self):
        for car in self.car_list:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
