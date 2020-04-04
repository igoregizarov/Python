class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def sum_mass(self):
        print(int(self._length * self._width * 25 * 5 / 1000), 'т.')


new_road = Road(20, 5000)
new_road.sum_mass()