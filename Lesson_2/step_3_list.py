mon = input('Введите номер месяца:\n')
seasons = ['зимой', 'весной', 'летом', 'осенью']

if mon.isnumeric() and int(mon) >= 1 and int(mon) <= 12:
    print('Этот месяц будет ' + str(seasons[(int(mon))//3 % 4]))
else:
    print('Нужно ввести номер месяца (от 1 до 12)')
