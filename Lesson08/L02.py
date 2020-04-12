class OwnError(Exception):
    pass


try:
    numb1 = int(input('Number #1 '))
    numb2 = int(input('Number #2 '))
    if numb2 == 0:
        raise OwnError('Деление на нуль!')
    res = numb1 / numb2
except ValueError:
    print('Введено не число!')
except OwnError as err:
    print(err)
else:
    print(f'{res}')
