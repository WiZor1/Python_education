def simple_division(num_1, num_2):
    try:
        print(float(num_1)/float(num_2))
    except ZeroDivisionError:
        print('делитель должен быть отличным от нуля\n')
    except Exception:
        print('Введите два числа через пробел\n')


numbers = input('Введите делимое и делитель через пробел:\n').split()
simple_division(numbers[0], numbers[1])
