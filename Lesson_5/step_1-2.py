f = open('new_file_1-2.txt', 'w+', encoding='utf-8')

print('\nWrite a frw strings to the file. Empty input is exit.\n')

while True:
    text = input()
    if text == '':
        f.seek(0)
        print('\nThe file', f.name, 'has',
              len([print(str(j) + ('-st' if j == 1 else '-nd' if j == 2 else '-th'),
                         'line has', len(i.split()), 'words.') for j, i in enumerate(f, 1)]), 'lines.')
        break
    f.write(text + '\n')
f.close()
