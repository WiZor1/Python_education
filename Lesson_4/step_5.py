from functools import reduce

print('Выводит произведение четных чисел от 100 до 1000:\n',
      reduce((lambda e_1, e_2: e_1 * e_2), [i for i in range(100, 1001)]))
