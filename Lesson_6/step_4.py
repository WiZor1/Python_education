class Car:
    speed = 0

    def __init__(self, color, name, is_police):
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print("Let's go with speed " + str(speed))

    def stop(self):
        self.speed = 0
        print('You need to stop')

    def turn(self, direct):
        if self.speed == 0:
            print('We stand')
        elif direct in ('right', 'left'):
            print('Turn ' + direct)
        else:
            print("I don't understand the direction")

    def info(self):
        print('This is ' + self.color + ' ' + self.name)

    def show_speed(self):
        print('Current speed is ' + str(self.speed))


class TownCar(Car):
    def __init__(self, color, name):
        super(TownCar, self).__init__(color, name, False)

    def go(self, speed):
        print("Your speed is higher than 60, but... ", end='') if speed > 60 else None
        super().go(speed)

    def show_speed(self):
        print("Your speed is higher than 60") if self.speed > 60 else None
        super().show_speed()


class SportCar(Car):
    def __init__(self, color, name):
        super(SportCar, self).__init__(color, name, False)


class WorkCar(Car):
    def __init__(self, color, name):
        super(WorkCar, self).__init__(color, name, False)

    def go(self, speed):
        print("Your speed is higher than 40, but... ", end='') if speed > 40 else None
        super().go(speed)

    def show_speed(self):
        print("Your speed is higher than 40") if self.speed > 40 else None
        super().show_speed()


class PoliceCar(Car):
    def __init__(self, color, name):
        super(PoliceCar, self).__init__(color, name, True)


town_car = TownCar('red', 'Town car')
sport_car = SportCar('blue', 'Sport car')
work_car = WorkCar('yellow', 'Word car')
police_car = PoliceCar('black', 'Police car')

town_car.info()
town_car.turn('left')
town_car.go(70)
town_car.turn('left1')
town_car.turn('left')
town_car.show_speed()
town_car.go(30)
town_car.show_speed()
town_car.stop()
print('------')
sport_car.info()
sport_car.go(70)
print('------')
work_car.info()
work_car.go(70)
print('------')
police_car.info()
police_car.go(70)
