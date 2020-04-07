class Cell:
    def __init__(self, count=int):
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        return Cell(self.count - other.count)

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def __str__(self):
        if self.count < 0:
            return 'Отрицательное значение'
        return f'{self.count}'

    def make_order(self, string):
        n = string
        for i in range(1, self.count + 1):
            if i > n:
                print()
                n += string
            i = '*'
            print(i, end='')


cell_1 = Cell(20)
cell_2 = Cell(25)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

cell_2.make_order(10)
