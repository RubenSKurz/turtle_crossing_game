import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
scoreboard = Scoreboard()
player = Player()
screen.listen()
screen.onkey(player.move_player, "w")

loop_count = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    loop_count += 1
    car_count = int(len(car_manager.car_list)-1)
    car_manager.car_move()
    if loop_count % 6 == 0:
        car_manager.spawn_car()
    if player.ycor() >= 280:
        player.next_level()
        scoreboard.show_level()
        car_manager.increase_speed()
    for car in car_manager.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
