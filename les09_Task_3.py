class Worker:
    def __init__(self, name, surname, position, income):
        self.my_list = [name, surname, position, income]


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f'{self.my_list[0]} {self.my_list[1]}'

    def get_total_income(self):
        return sum((val for i, val in self.my_list[3].items()))


# Проверка:
w_1 = Position('Павел', 'Богданов', 'Генеральный директор', {'wage': 250000, 'bonus': 150000})
print(w_1.get_full_name(), ' - {:,g}'.format(w_1.get_total_income()).replace(',', ' '))
#
w_2 = Position('Иван', 'Васильев', 'Инженер', {'wage': 100000, 'bonus': 50000})
print(w_2.get_full_name(), ' - {:,g}'.format(w_2.get_total_income()).replace(',', ' '))
