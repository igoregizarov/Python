import json
import codecs

with open('text7.txt', 'r', encoding='utf-8') as f_obg:
    averedg_pribil = 0
    max_pribil = 0
    i = 0
    dict_1 = {}
    for line in f_obg:
        line = line[:-1]
        print(line)
        line = line.split(' ')
        pribil = int(line[-2]) - int(line[-1])
        print(f'Выручка компании {line[0]} составила: {pribil}.')
        new_dict = {line[0]: pribil}
        dict_1.update(new_dict)
        if pribil > 0:
            max_pribil += pribil
            i += 1
    averedg_pribil = max_pribil / i
    print('Средняя выручка составила - ', averedg_pribil)
    dict_2 = {'average_profit': averedg_pribil}
    end_list = [dict_1, dict_2]
    print(end_list)

with codecs.open('my_file.json', 'w', encoding='utf-8') as write_f:
    json.dump(end_list, write_f, ensure_ascii=False)
