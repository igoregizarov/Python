n = 1
n_max = int(input('Укажите количество товаров:'))
a =[]
b = []
c = []
d = ['шт.']
goods = []
while n <= n_max:
    name = input(f'Укажите наименование товара {n}: ')
    prise = int(input(f'Укажите цену товара {n}: '))
    count = int(input(f'Укажите количество товара {n}: '))
    good =(n, {'название': name, 'цена': prise, 'количество': count, 'ед': 'шт'})
    goods.append(good)
    a.append(name)
    b.append(prise)
    c.append(count)
    n += 1
print(goods)

my_dict ={
    'название': a,
    'цена': b,
    'количество': c,
    'ед': d
}
print(my_dict)