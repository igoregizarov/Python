main_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list1 = [main_list[el] for el in range(len(main_list)) if main_list[el] > main_list[el - 1]]

print(main_list)
print(new_list1)
