a = int(input('Результат за первый день: '))
b = int(input('Общий результат: '))
n = 1
while True:
	print('{}-й день: {:.2f}'.format(n, a))
	if a > b:
		break
	n += 1
	a = a + (a * 0.1)
print('На {}-й день спортсмен достиг результата - не менее {:.2f} км.'.format(n, a))