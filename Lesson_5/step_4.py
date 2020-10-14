try:
    from googletrans import Translator
    tra = Translator()
    with open('text_4.txt', 'r', encoding='utf-8') as fr, open('text_4_w.txt', 'w', encoding='utf-8') as fw:
        for i in fr.readlines():
            i = i.split()
            i[0] = tra.translate(i[0], src='en', dest='ru').text
            fw.write(' '.join(i) + '\n')
except ModuleNotFoundError:
    print('Please install the "googletrans" lib ("pip install googletrans" in CMD)')
