num_sum = 0
next_step = True


def growing_sum(_sum, new_list):
    step_sum = 0
    _next = True
    try:
        for i in range(len(new_list) - 1):
            new_list[i] = int(new_list[i])
        step_sum = sum(new_list[:-1])
    except Exception:
        print('Нужно ввести числа через пробел')
    try:
        step_sum += int(new_list[-1])
    except Exception:
        if new_list[-1] == 'q':
            _next = False
    return _sum + step_sum, step_sum, _next


while next_step:
    numbers = input('Введите ряд чисел через пробел. Для выхода в конце введите "q"\n').split()
    num_sum, s_sum, next_step = growing_sum(num_sum, numbers)
    if next_step:
        print(str(num_sum) + '(' + str(s_sum) + ')')
    else:
        print(str(num_sum))
