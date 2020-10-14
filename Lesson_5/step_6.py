'''les_dict = dict()
with open('text_6.txt', 'r', encoding='utf-8') as f:
    for _str in f:
        les_dict[_str.split()[0][:-1]] = sum([int(i[:i.index('(')]) if i != '-' else 0 for i in _str.split()[1:]])
print(les_dict)'''

'''

Выше более полная структура, но после ее реализации захотелось сократить. А можно ли как-то открытие-закрытие файла
скомпоновать в генератор?

'''


with open('text_6.txt', 'r', encoding='utf-8') as f:
    print({_str.split()[0][:-1]: sum([int(i[:i.index('(')]) if i != '-' else 0 for i in _str.split()[1:]])
           for _str in f})
