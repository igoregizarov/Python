array = input('Введите слова через пробел: ')
array = array.split()

n = 1
for i in array:
    print(f'{n}) {i}')
    n += 1
    if n > 10:
        break
