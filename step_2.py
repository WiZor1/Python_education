seconds = int(input('Введите время в секундах:\n'))
print(f'Преобразованное время: {((seconds-seconds%3600)//3600)%24}:{((seconds-seconds%60)//60)%60}:{seconds%60}')
