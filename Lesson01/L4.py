number = int(input('Введите целое положительное число: '))
print (number)
max_n = number % 10
while number > 0:
	number = int(number / 10)
	next_n = number % 10
	if max_n < next_n:
		max_n = next_n
print(max_n)