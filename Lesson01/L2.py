hour = 0
minut = 0
seconds = 0
time = int(input('Введите время в секундах '))
if time > 3600:
	hour = int(time / 3600)
minut = int(((time - (hour * 3600)) / 60))	
seconds = time - ((hour * 3600) + (minut * 60))
if hour < 9:
	hour = '0' + str(hour)
if minut < 9:
	minut = '0' + str(minut)
if seconds < 9:
	seconds = '0' + str(seconds)
print (f'{hour}:{minut}:{seconds}')