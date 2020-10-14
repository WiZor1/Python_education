with open('text_3.txt', 'r', encoding='utf-8') as f:
    print('\n'.join([' получает '.join(i.replace('\n', '').split()) for i in f if
                     float(i.replace('\n', '').split()[1]) > 20000]))
    f.seek(0)
    print('\nСредняя плата (при > 20000):', (lambda x: sum(x)/len(x))(
        [float(i.replace('\n', '').split()[1]) for i in f if float(i.replace('\n', '').split()[1]) > 20000]))
    f.seek(0)
    print('\nСредняя плата:', (lambda x: sum(x) / len(x))([float(i.replace('\n', '').split()[1]) for i in f]))
