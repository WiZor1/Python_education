def simple_negative_pow(base, exp):
    try:
        base = float(base)
        exp = int(exp)
    except ValueError:
        return 'Должны быть введены два числа (действительное и целое отрицательное)'
    if exp > 0 and base < 0:
        return 'Должны быть введены два числа (действительное и целое отрицательное)'
    else:
        return base**exp


def advance_negative_pow(base, exp):
    try:
        base = float(base)
        exp = int(exp)
    except ValueError:
        return 'Должны быть введены два числа (действительное и целое отрицательное)'
    ans = 1
    if exp > 0 and base < 0:
        return 'Должны быть введены два числа (действительное и целое отрицательное)'
    else:
        for multi in range(-exp):
            ans = ans * 1 / base
            multi += multi
        return ans


numbers = input('Введите 2 числа через пробел:\n').split()
print(simple_negative_pow(numbers[0], numbers[1]))
print(advance_negative_pow(numbers[0], numbers[1]))
