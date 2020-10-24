from random import randint
import re


class Date:
    """
    Можно было применять @property для фильтрафии, но в данной ситуации мне показалось лучше обойтись без него,
    иначе добавляем еще несколько функций-значений
    """
    day, month, year = False, False, False

    def __init__(self, date):
        self.date = date

    @classmethod
    def date_from_str(cls, obj):
        print('Изначальная строка:', obj.date)
        reg = re.compile(r'[^\d]+')
        obj.day, obj.month, obj.year = [int(i) for i in reg.sub(' ', obj.date).split()]

    @staticmethod
    def value_val(date):
        if date.day not in range(1, 32):
            date.day = 31 if date.day - 31 > 1 - date.day else 1
            print('Значение дня должно лежать впромежутке от 1 до 31. Ставим значение по умолчанию')
        if date.month not in range(1, 13):
            date.month = 12 if date.month - 12 > 1 - date.month else 1
            print('Значение месяца должно лежать впромежутке от 1 до 12. Ставим значение по умолчанию')
        if date.year not in range(1970, 2021):
            date.year = 2020 if date.year - 2020 > 1970 - date.year else 1970
            print('Значение года должно лежать впромежутке от 1970 до 2020. Ставим значение по умолчанию')
        print('День:', date.day, '\nМесяц:', date.month, '\nГод:', date.year)


dt_1 = Date(str(randint(1, 40)) + '  ' + str(randint(1, 15)) + '-' + str(randint(1900, 2200)))
dt_1.date_from_str(dt_1)
dt_1.value_val(dt_1)
