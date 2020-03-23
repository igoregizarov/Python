my_list = [7, 5, 3, 3, 2]
print(my_list)
n = int(input("Enter number: "))
if n > my_list[0]:
    my_list.insert(0, n)
elif n < my_list[-1]:
    my_list.append(n)
else:
    i = my_list.index(n)
    count = my_list.count(n)
    my_list.insert(i + count, n)
print(my_list)