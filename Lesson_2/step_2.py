my_list = input("Введите ряд значений через запятую: ")
# my_list = '1,2, 3, 4 ,5,  6 , 7'
my_list = ' '.join(my_list.split()).replace(', ', ',').replace(' ,', ',').split(',')

res_list = my_list[::2]
for le in range(len(my_list[1::2])):
    res_list.insert(2*le, my_list[2*le+1])
print('Ой, кто-то перемешал значения, соседние элементы поменялись местами: ' + ', '.join(res_list))
