from sys import argv

"""
var_1 - выроботка в часах
var_2 - ставка в час
var_3 - премия
"""

try:
    script_name, var_1, var_2, var_3 = argv
    result = (float(var_1) * float(var_2)) + float(var_3)
    print("Зароботная плата составила", result)

except ValueError:
    print('Введены не корректные параметры!')
