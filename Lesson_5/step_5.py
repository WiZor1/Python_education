with open('text_5.txt', 'w+', encoding='utf-8') as f:
    f.write(input('Enter numbers separated by space. Any letter is exit.\n'))
    f.seek(0)
    print(sum([float(i) for i in f.read().split()]))
