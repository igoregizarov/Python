class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.surname, self.name)

    def get_total_income(self):
        print(sum(self._income.values()))


new_worker = Position('Ivan', 'Ivanov', 'Driver', 1000, 100)
new_worker.get_full_name()
new_worker.get_total_income()
