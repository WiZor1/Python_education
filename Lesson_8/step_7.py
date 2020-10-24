class Complex:
    def __init__(self, x):
        x = x.split()
        try:
            x = [float(x[0]), float(x[1] + x[2][:-1]) if len(x) == 3 else 0]
            self.x = x
        except Exception as er:
            print(er)
            print('Complex format: x + yj')

    def __add__(self, other):
        return Complex(str(self.x[0] + other.x[0]) +
                       (' + 'if self.x[1] + other.x[1] > 0 else ' - ') + str(abs(self.x[1] + other.x[1])) + 'j')

    def __mul__(self, other):
        return Complex(str(self.x[0] * other.x[0] - self.x[1] * other.x[1]) +
                       (' + 'if self.x[0] * other.x[1] + self.x[1] * other.x[0] > 0 else ' - ') +
                       str(abs(self.x[0] * other.x[1] + self.x[1] * other.x[0])) + 'j')

    def __str__(self):
        return str(self.x[0]) + (' - ' if self.x[1] < 0 else ' + ') + str(abs(self.x[1])) + 'j'


a = Complex('-4')
print(a)
b = Complex('3 - 6j')
print(b)
print('Сложение:', a + b)
print('Умножение:', a * b)
