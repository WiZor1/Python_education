import re


class MyExc(Exception):
    def __init__(self, text):
        self.text = text


num_list = []

print('Введите числовое значение:\n')
while (value := input()) != 'stop':
    try:
        value = value.split()
        if not min((i.isdigit() for i in value)):
            reg = re.compile(r'[^\d.]+')
            value = [reg.sub('', i) for i in value]
            for i in range(value.count('')):
                value.remove('')
            num_list += [float(i) for i in value]
            raise MyExc('Введено буквенное значение, ожидалось числовое. Для выхода введите "stop" или продолжайте '
                        'вводить числа')
        else:
            num_list += [float(i) for i in value]
    except MyExc as er:
        print(er)
    except Exception as er:
        print(er)

print(num_list)
