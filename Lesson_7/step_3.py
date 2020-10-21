class Cell:
    def __init__(self, nucleus):
        if nucleus >= 0:
            self.nucleus = nucleus
        else:
            raise IOError('Количество ячеек не может быть отрицательным количеством')

    def __add__(self, other):
        return Cell(self.nucleus + other.nucleus)

    def __sub__(self, other):
        if self.nucleus < other.nucleus:
            raise IOError('В результате вычитания получается отрицательное количество ячеек')
        else:
            return Cell(self.nucleus - other.nucleus)

    def __mul__(self, other):
        return Cell(self.nucleus * other.nucleus)

    def __truediv__(self, other):
        return Cell(round(self.nucleus / other.nucleus, 0))

    def __str__(self):
        return str(int(self.nucleus))

    def make_order(self, n):
        print(self)
        for i in range(int(self.nucleus)):
            print('*', end='\n' if i % n == n - 1 else '')
        print('\n')


cell1, cell2, cell3, cell4 = Cell(12), Cell(5), Cell(4), Cell(6)

((cell1 + cell2 - cell3) / cell3 * cell4).make_order(5)
