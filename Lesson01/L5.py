#Выручка - revenue
#Издержки - costs
#Рентабельность - profitability
revenue = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))
fin_result = revenue - costs
if fin_result >= 0:
	print (f'Прибыль составляет {fin_result}.')
	profitability = fin_result / revenue
	print(f'Рентабельность составляет {profitability}.')
	persons = int(input('Укажите численность сотрудников: '))
	fin_for_person =  fin_result / persons
	print(f'Прибыль в расчете на одного сотрудника составляет {intfin_for_person}.')
else:
	print (f'Убыток составляет {fin_result}.')