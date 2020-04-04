import random


class Car:
    def __init__(self, color, name, is_police):
        self.color = color
        self.name = name
        self.is_police = is_police

    speed = int

    def go(self):
        print(f'Машина {self.name}, цвет {self.color} поехала!')

    def stop(self):
        print(f'Машина {self.name}, цвет {self.color} остановилась!')

    def turn_left(self):
        print(f'Машина {self.name}, цвет {self.color} повернула на лево!')

    def turn_right(self):
        print(f'Машина {self.name}, цвет {self.color} повернула на право!')

    def show_speed(self):
        self.speed = random.randint(0, 200)
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        self.speed = random.randint(0, 200)
        print(self.speed)
        if self.speed > 60:
            print("Скорость превышена!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        self.speed = random.randint(0, 200)
        print(self.speed)
        if self.speed > 40:
            print("Скорость превышена!")


class PoliceCar(Car):
    pass


car_1 = TownCar('black', 'Lexus', False)
print(car_1.name)
print(car_1.color)
print(car_1.is_police)
car_1.go()
car_1.turn_left()
car_1.stop()
car_1.show_speed()

car_2 = SportCar('red', 'Lamborghini', False)
print(car_2.name)
print(car_2.color)
print(car_2.is_police)
car_2.go()
car_2.turn_right()
car_2.stop()
car_2.show_speed()

car_3 = WorkCar('white', 'MAN', False)
print(car_3.name)
print(car_3.color)
print(car_3.is_police)
car_3.go()
car_3.turn_right()
car_3.stop()
car_3.show_speed()

car_4 = PoliceCar('blue', 'Lada', True)
print(car_4.name)
print(car_4.color)
print(car_4.is_police)
car_4.go()
car_4.turn_left()
car_4.stop()
car_4.show_speed()