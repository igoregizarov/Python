def fact(number):
    n = 1
    for i in range(1, number + 1):
        n *= i
        yield n


number = int(input("Факториал какого числа?"))
for _ in fact(number):
    if _ > 15:
        break
    print(_)