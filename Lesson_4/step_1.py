from sys import argv

'''
Параметры:
    Первый - выработка в часах
    Второй - ставка в час
    Третий - премия

'''

try:
    print('Общая плата для сотрудника:', int(argv[1]) * float(argv[2]) + float(argv[3]))
except IndexError:
    print('При запуске расчета необходимо ввести 3 параметра через пробел: выработка в часах, ставка в час,'
          ' фиксированная премия')
except ValueError:
    print('Пожалуйста, введите численные значения')
except Exception as err:
    print(err)
