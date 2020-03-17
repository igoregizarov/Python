a = int(input('Результат за первый день: '))
b = int(input('Общий результат: '))
n = 1
while True:
	print(f'{n}-й день: {a}')
	if a > b:
		break
	n += 1
	a = a + (a * 0.1)
print(f'На {n}-й день спортсмен достиг результата - не менее {int(a)} км.')