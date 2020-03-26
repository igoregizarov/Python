"""Функция возведения в степень"""
"""Способ №1"""
x = 2
y = -2


def my_func(var_1, var_2):
    print(var_1 ** var_2)


my_func(x, y)

"""Способ №2"""


def my_func_new(var_1, var_2):
    for i in range(abs(var_2)):
        var1 = var_1 * var_1
    return print(var_1 ** var_2)


my_func_new(x, y)
