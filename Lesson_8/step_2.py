class MyZeroDivExc(ZeroDivisionError):
    def __init__(self, text):
        self.text = text


while True:
    try:
        a, b = [int(i) for i in input('Введите 2 числа через пробел\n').split()]
        if not b:
            raise MyZeroDivExc('Выявлено деление на 0')
        print(a / b)
        break
    except MyZeroDivExc as er:
        print(er)
    except Exception as er:
        print('Что-то пошло не так:', er)

