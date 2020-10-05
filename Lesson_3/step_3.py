def my_func(num_1, num_2, num_3):

    try:
        numbers = [int(num_1), int(num_2), int(num_3)]
    except (TypeError, ValueError):
        numbers = [0, 0, 0]
        print('Должны быть введены числа')
    numbers.remove(min(numbers))
    return numbers[0] + numbers[1]


numbers = input('Через пробел 3 числа:\n').split()
print(my_func(numbers[0], numbers[1], numbers[2]))
