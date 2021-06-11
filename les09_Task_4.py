class Car:
    speed_limit = {'TownCar': 60, 'WorkCar': 40}

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed} км/час')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'Текущая скорость: {self.speed} км/час')
        limit_for_car = self.speed_limit.get(self.__class__.__name__)
        if limit_for_car is not None:
            if self.speed > limit_for_car:
                print(f'Превышение допустимой скорости на {self.speed - limit_for_car} км/час')

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'Текущая скорость: {self.speed} км/час')
        limit_for_car = self.speed_limit.get(self.__class__.__name__)
        if limit_for_car is not None:
            if self.speed > limit_for_car:
                print(f'Превышение допустимой скорости на {self.speed - limit_for_car} км/час')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

# --- Машина 1 ---
print('\n---- Car №1 ----')
car_1 = TownCar(65, 'Красный', 'Lexus')
print(car_1.color, car_1.name, f'Полиция: {"да" if car_1.is_police else "нет"}',
      f'Cкорость: {car_1.speed}', sep='\n')
car_1.go()
car_1.stop()
car_1.turn('направо')
car_1.show_speed()

# --- Машина 2 ---
print('\n---- Car №2 ----')
car_2 = PoliceCar(125, 'Черный', 'Mersedes')
print(car_2.color, car_2.name, f'Полиция: {"да" if car_2.is_police else "нет"}',
      f'Cкорость: {car_2.speed}', sep='\n')
car_2.go()
car_2.stop()
car_2.turn('налево')
car_2.show_speed()


# --- Машина 3 ---
print('\n---- Car №3 ----')
car_3 = WorkCar(49, 'Желтый', 'Toyota')
print(car_3.color, car_3.name, f'Полиция: {"да" if car_3.is_police else "нет"}',
      f'Cкорость: {car_3.speed}', sep='\n')
car_3.go()
car_3.stop()
car_3.turn('направо')
car_3.show_speed()
