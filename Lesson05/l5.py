while True:
    my_f = open("sum_number.txt", "w", encoding="utf-8")
    try:
        my_list = ''.join(input('Enter number with space: ')).split(' ')
        new_list = []
        for i in range(len(my_list)):
            a = int(my_list[i])
            new_list.append(a)
            my_f.write(my_list[i])
            my_f.write(' ')
        print(sum(new_list))
        break
    except ValueError:
        print('Is not a number')
my_f.close()
