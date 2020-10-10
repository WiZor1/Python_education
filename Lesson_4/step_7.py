from functools import reduce


def fact(n):
    if not int(n):
        n = '1'
    for y in range(1, int(n) + 1):
        yield reduce((lambda x1, x2: x1 * x2), [i for i in range(1, y + 1)])


for el in fact(input('Факториал до какого числа необходимо получить?\n')):
    print(el)
