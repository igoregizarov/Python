class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки!')


class Pen(Stationery):

    def draw(self):
        print(f'Запуск отрисовки! Поможет {self.title}.')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки! Поможет {self.title}.')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки! Поможет {self.title}.')


tool_1 = Pen('ручка')
tool_1.draw()

tool_2 = Pencil('карандаш')
tool_2.draw()

tool_3 = Handle('маркер')
tool_3.draw()