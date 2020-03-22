my_list = input('Enter number ')
my_list = my_list.split()
new_list = []
n = 0
for i in my_list:
    if n % 2 == 0:
        new_list.append(my_list[n + 1])
        new_list.append(my_list[n])
    n += 1
    if n + 1 == len(my_list):
        if n % 2 == 0:
            new_list.append(my_list[n])
        break
print(new_list)


