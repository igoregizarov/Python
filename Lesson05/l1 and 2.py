name = input('Укажите имя файла для создания.\n') + '.txt'
print(name)
my_f = open(name, 'w')
n = 1
while True:
    string = input(f'Enter string {n}: ')
    if string == '':
        break
    my_f.write(f'{string}\n')
    n += 1

with open(name, 'r') as my_f:
    content = my_f.read()
    print(content)

with open(name) as new_f:
    content = new_f.readlines()
    count_str = len(content)  # количество строк
sum_word = 0
print(f'В файле {name} {len(content)} строк(и).')
for i in range(1, count_str + 1):
    count_word = len(content[-1 + i].split())
    print(f'В строке №{i} количество слов = {count_word}')
    i += 1
    sum_word += count_word
print('Общее количество букв', sum_word)