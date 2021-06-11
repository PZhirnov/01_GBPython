from time import sleep
from itertools import cycle
from turtle import *


class TrafficLight:
    __color = 'green'

    def running(self, color_control):
        current_condition = cycle(color_control)
        while True:
            color, time, font_color = next(current_condition)
            self.__color = color  # сохраним состояние
            print(f'{font_color} {color} - {time} сек.')
            self.color_show()
            sleep(time)

    def color_show(self):
        position()
        speed(300)
        setx(-0)
        sety(-200)
        begin_fill()
        color('red', self.__color)
        circle(200)
        end_fill()


# предполагаю, что в класс передаются параметры управления в виде кортежа
color_time_control = (('red', 7, '\033[31m'), ('yellow', 2, '\033[33m'),
                      ('green', 10, '\033[32m'), ('yellow', 3, '\033[33m'))

a = TrafficLight()
a.running(color_time_control)
