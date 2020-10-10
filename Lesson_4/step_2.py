from random import randrange

print('Выводит числа больше предыдущих в списке.\n')

# my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list = [randrange(300) for i in range(randrange(20))]

print('Исходный список:', my_list, '\nПреобразованный список:',
      [my_list[i] for i in range(len(my_list)) if my_list[i] > (my_list + [my_list[0]+1])[i-1]])
