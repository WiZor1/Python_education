class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_weight(self, depth):
        '''
        Возвращает кол-во тонн дороги заданной толщины
        '''
        return round(self._length * self._width * 25 * depth / 1000, 2)


new_road = Road(5000, 20)
print(new_road.get_weight(5))
