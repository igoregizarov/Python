from itertools import count, cycle

print('Генератор целых чисел')
n_min = int(input('Скакого числа начать: '))
n_max = int(input('Каким закончить: '))
my_list = []
for el in count(n_min):
    my_list.append(el)
    print(el)
    if el == n_max:
        break
print(my_list)
for el in cycle(my_list):
    print(el)
    if el == my_list[-1]:
        break
