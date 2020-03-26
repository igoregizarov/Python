def func(arg1, arg2):
    try:
        print(arg1 / arg2)
    except ZeroDivisionError:
        print('Деление на ноль запрещено!!!')


func(int(input('Number №1: ')), int(input('Number №2: ')))

