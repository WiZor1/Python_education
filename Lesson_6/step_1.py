import time


def cls(n):
    time.sleep(n)
    print("\n" * 50)


class TrafficLight:
    __color = {'red': '\033[31m0\033[0m\n0\n0', 'yellow': '0\n\033[33m0\033[0m\n0', 'green': '0\n0\n\033[32m0\033[0m'}

    def light(self, col):
        print(self.__color[col])

    def running(self, red, yellow, green):
        while True:
            cls(0)
            self.light('red')
            cls(red)
            self.light('yellow')
            cls(yellow)
            self.light('green')
            cls(green)
            self.light('yellow')
            cls(yellow)


new_light = TrafficLight()
new_light.running(4, 1, 4)
