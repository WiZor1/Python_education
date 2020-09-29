number = int(input('Введите число:\n'))
max_numeral = 0
while number != 0:
    if number % 10 > max_numeral:
        max_numeral = number % 10
    number //= 10
print('Максимальная цифра в введенном числе:', max_numeral)
