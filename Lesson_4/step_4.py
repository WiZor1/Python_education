from random import randrange

print('Вывести уникальные числа в исходном порядке.\n')

# my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_list = [randrange(15) for i in range(randrange(20))]

print('Исходный список:', my_list, '\nПреобразованный список:',
      [i for i in my_list if my_list.count(i) == 1])
