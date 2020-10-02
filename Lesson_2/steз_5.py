print('Для выхода введите "exit".\n')
rate_list = []
rate = input('Поставьте оценку:\n')
while rate.lower() != 'exit':
    if rate.isnumeric() and int(rate) >= 1 and int(rate) <= 10:
        rate = int(rate)
        if len(rate_list) == 0:
            rate_list.append(rate)
        else:
            for i, elem in enumerate(rate_list):
                if elem < rate:
                    rate_list.insert(i, rate)
                    break
                elif len(rate_list) == i+1:
                    rate_list.append(rate)
                    break
        print(rate_list)
    else:
        print('У нас система оценки от 1 до 10.')
    rate = input('Поставьте оценку:\n')
