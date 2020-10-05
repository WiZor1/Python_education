def int_func(word):
    return word.title()


print(int_func(input('Введите слово или предложение:\n')))

'''
Программа уже выполняет то, о чем говорится в доп. задании. Но я подозреваю, имелось в виду то, что реализовано ниже
'''

word_list = input('Введите предложение:\n').split()
for word in word_list:
    print(int_func(word) + ' ', end='')
