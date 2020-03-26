a = int(input('Число №1 '))
b = int(input('Число №2 '))
c = int(input('Число №3 '))


def func_sum(var_1, var_2, var_3):
    my_list = [var_1, var_2, var_3]
    var_del = min(my_list)
    my_list.remove(var_del)
    return print(sum(my_list))


func_sum(a, b, c)