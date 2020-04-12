class OwnError(Exception):
    pass


class Stock:
    def __init__(self, area=0):
        self.area = area
        self.volume = area * 5

    def get_in(self, a, b):
        self.d = {a: b}
        return self.d

    def get_out(self, a):
        return new_d.get(a)


class Equipment:
    def __init__(self, name, weight, prise, count):
        self.name = name
        self.weight = weight
        self.prise = prise
        self.count = count


class Printer(Equipment):
    def __init__(self, name, weight, prise, count, color_paint, ):
        super().__init__(name, weight, prise, count)
        self.color_paint = color_paint


class Scaner(Equipment):
    def __init__(self, name, weight, prise, count, displey):
        super().__init__(name, weight, prise, count)
        self.displey = displey


class Xerox(Equipment):
    def __init__(self, name, weight, prise, count, black_paint):
        super().__init__(name, weight, prise, count)
        self.black_paint = black_paint


class_1 = Printer('Принтер', 2.5, 1000, 5, True)
class_2 = Scaner('Сканер', 3, 2000, 15, True)
class_3 = Xerox('Ксерокс', 5, 10000, 2, True)
m = Stock()
new_d = {}
n_list = []
ofice = ['Администрация', 'ОДС', 'ТО']
for i in range(len(ofice)):
    print(f'Отдел номер {i + 1} - {ofice[i]}')

new_d.update(m.get_in(class_1.name, class_1.count))
new_d.update(m.get_in(class_2.name, class_2.count))
new_d.update(m.get_in(class_3.name, class_3.count))
print(new_d)
x_word = None
while x_word != 'q':
    while True:
        name_tex = input('Укажите наименование техники - ')
        if new_d.get(name_tex) == None:
            print('Не верное наименование!')
        elif new_d[name_tex] == 0:
            print('Нет товара на складе!')

        else:
            break

    somethin_count = m.get_out(name_tex)
    print(f'Количество товара на складе {somethin_count}')
    while True:
        try:
            somethin_ofice = int(input('В какой отдел передать?укажите номер "1, 2, 3" - '))
            if somethin_ofice < 1 or somethin_ofice > 3:
                print('Нет такого отдела!')
            else:
                break
        except ValueError:
            print('Введено не число!!!')
    while True:
        try:
            count = int(input('Сколько шт? - '))
            new_d[name_tex] = new_d[name_tex] - count
            if new_d[name_tex] < 0:
                print(new_d[name_tex])
                new_d[name_tex] = new_d[name_tex] + count
                print('Недостаточно товара на складе')
            else:
                break
        except ValueError:
            print('Введено не число!!!')
    print(f'В отдел {ofice[somethin_ofice - 1]} передано {count} шт - {name_tex}.')
    #     new_d[name_tex] = new_d[name_tex] - count
    print(f'Остаток - {new_d}')
    if sum(new_d.values()) == 0:
        print('На складе нет остатков!')
        break

    x_word = input('Чтобы закончить введите "q"')
print('До свидания')