import json

with open('text_7.txt', 'r', encoding='utf-8') as f:
    print(profit_dict := {i.replace('\n', '').split()[0]: (lambda x: int(x[-2]) - int(x[-1]))
    (i.replace('\n', '').split()) for i in f.readlines()})
print(profit_dict := [profit_dict, {'average_profit': (lambda x: sum(x)/len(x))([prof for prof in profit_dict.values() if prof > 0])}])

with open('text_7_r.json.json', 'w', encoding='utf-8') as json_w:
    json_w.write(json.dumps(profit_dict, ensure_ascii=False, indent=4))
