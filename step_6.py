by_day = int(input('Сколько спортсмен пробежал в первый день?\n'))
inc = int(input('Сколько нужно пробежать?\n'))
day_num = 1

while by_day <= inc:
    print(str(day_num) + f'-й день: {by_day:.2f}')
    by_day *= 1.1
    day_num += 1
print('На', str(day_num) + '-й день  спортсмен достиг результата — не менее', inc,'км')
