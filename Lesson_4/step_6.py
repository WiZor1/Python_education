from itertools import count, cycle

try:
    num_of_cycles = int(input('Сколько циклов по 3 буквы выводить?\n'))
    try:
        for i, numeric_cycle in enumerate(count(0)):
            try:
                for j, char_cycle in enumerate(cycle('AM')):
                    print(numeric_cycle, chr(ord(char_cycle) + j))
                    _pass = 1 / (j - 2)
            except ZeroDivisionError:
                pass
            _pass = 1 / (i + 1 - num_of_cycles)
    except ZeroDivisionError:
        pass
except ValueError:
    print('Нужно ввести одно число')
