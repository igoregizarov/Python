x_word = True
def func_sum():
    global x_word
    a = input('Number: ')
    list_a = a.split(' ')
    new_list = []
    for i in list_a:
        if i.upper() == 'Q':
            x_word = False
            break
        try:        
            new_list.append(int(i))
        except TypeError:
            print('Введено не число!!!')
        except ValueError:
            print('Введено не число!!!')
            
    
    return sum(new_list)
    
res = 0
while x_word == True:
    print ('Введите числа через пробел. Для выхода введите "Q"')    
    max_s = func_sum()
    res = max_s + res
    print(res)