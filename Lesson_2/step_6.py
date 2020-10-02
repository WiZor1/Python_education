print('Для выхода введите "exit".\n')

choice = input('Что вы хотите сделать?\n\t1. Просмотреть товары\n\t2. Добавить товар\n\t3. Удалить товар\n\t4. Показать'
               ' аналитические данные\n\t5. Закрыть диалоговое окно\n\t6. Служебная информация (структура каталога)'
               '\n\n')
store = []
max_id = 0
header = ''
product_str = ''
id_list = set()
content = (['название', 's'], ['цена', 'n'], ['количество', 'n'], ['ед', 's'])
for param in content:
    header = f'{header:20}{param[0]:20}'
single_prod = {}
max_letters = 15
while True:

    if 'осмотреть' in choice or choice == '1':
        if len(store) == 0:
            print('В каталог не добавлено ни одного товара\n\n')
        else:
            print('Товаров в каталоге:', len(store), '\n' + header)
            for prod in store:
                for param in prod[1].values():
                    product_str = f'{product_str:20}{param:20}'
                print(product_str)
                product_str = ''
    elif 'добавить' in choice.lower() or choice == '2':
        for param in content:
            val = input('\nВведите значение для параметра ' + param[0] + ':\n')
            if param[1] == 'n' and not val.isnumeric():
                while not val.isnumeric():
                    val = input('Пожалуйста, введите целое число (да, даже для цены):\n')
            single_prod.update({param[0]: val})

        store.append((max_id + 1, single_prod))
        id_list.add(max_id + 1)
        max_id += 1
        print(f'Добавлено: ' + single_prod[content[0][0]] + '\n\n')
        #        print(single_prod[content[0][0]])
        single_prod = {}
    elif 'удалить' in choice.lower() or choice == '3':
        if len(store) == 0:
            print('В каталоге нет товаров\n')
        else:
            print('Товары в каталоге:\n')
            print('id    ' + f'{content[0][0]:20}')
            for prod in store:
                # for param in prod[1].values():
                print(f'{prod[0]}     {prod[1][content[0][0]]:20}')
            delete_num = input('Введите номер того, который хотите убрать (-1 для возврата):\n')
            if delete_num.isnumeric() and int(delete_num) in id_list:
                delete_num = int(delete_num)
                for i, prod in enumerate(store):
                    if prod[0] == delete_num:
                        print(prod[1][content[0][0]] + ' удален')
                        id_list.discard(delete_num)
                        store.pop(i)
            elif delete_num.isnumeric():
                print('Товара не найдено\n')
                continue

    elif 'закрыть' in choice.lower() or choice == '5' or choice == 'exit' or 'выйти' in choice.lower():
        break
    elif 'аналити' in choice.lower() or choice == '4':
        print('Краткие аналитические данные по разнообразию товара (раздел в доработке =) ):\n')
        stat_dict = dict()
        for param in content:
            param_values = set()
            for prod in store:
                param_values.add(prod[1][param[0]])
            stat_dict.update({param[0]: param_values})
        print(stat_dict)
    elif choice == '6':
        print(store)
    else:
        print('Я вас не понимаю :( если хотите выйти, введите "exit", 5, "закрыть" или "выйти"\n')
    input('\nДля продолжения нажмите клавишу ввода...\n')
    choice = input('Что вы хотите сделать?\n\t1. Просмотреть товары\n\t2. Добавить товар\n\t3. Удалить товар\n\t'
                   '4. Показать аналитические данные\n\t5. Закрыть диалоговое окно\n\t'
                   '6. Служебная информация (структура каталога)\n\n')
