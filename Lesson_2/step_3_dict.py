mon = input('Введите номер месяца:\n')
seasons = {1: 'зимой', 2: 'весной', 3: 'летом', 4: 'осенью'}

if mon.isnumeric() and int(mon) >= 1 and int(mon) <= 12:
    print('Этот месяц будет ' + str(seasons[(int(mon))//3 % 4 + 1]))
else:
    print('Нужно ввести номер месяца (от 1 до 12)')
