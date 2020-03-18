#Выручка - revenue
#Издержки - costs
#Рентабельность - profitability
revenue = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))
fin_result = revenue - costs
if fin_result > 0:
	print (f'Прибыль составляет {fin_result}.')
	profitability = fin_result / revenue
	print(f'Рентабельность составляет {profitability}.')

else:
	print (f'Убыток составляет {fin_result}.')
persons = int(input('Укажите численность сотрудников: '))
fin_for_person =  fin_result / persons
print(f'Прибыль в расчете на одного сотрудника составляет {fin_for_person}.')