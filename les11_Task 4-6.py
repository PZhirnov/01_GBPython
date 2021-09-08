from pprint import pprint
from abc import ABC, abstractmethod


class Warehouse:
    def __init__(self):
        self.war_house = {}
        self.id_group = {}  # храним сопоставление групп и ID для ускорения поиска
        self.id_equipment = 0  # уникальный ID объекта на складе
        self.id_err = 0  # уникальный номер ошибки в логе
        self.log_err = {}  # лог данных с ошибками, чтобы не терялись

    # отправляем товар на склад
    def send_to_wh(self, equipment):
        self.id_equipment += 1
        data_valid = equipment.all_data().copy()
        # простая валидация данных - количество и стоимость
        if isinstance(data_valid[2], str) or isinstance(data_valid[3], str):
            try:
                data_valid[2] = int(data_valid[2])
                data_valid[3] = int(data_valid[3])
            except ValueError:
                self.log_error(data_valid, self.id_equipment)
                return None
        self.war_house.setdefault(equipment.name_obj, {})
        update_data = self.war_house.get(equipment.name_obj)
        update_data[self.id_equipment] = data_valid
        self.id_group[self.id_equipment] = equipment.name_obj

    #  Сохраняем данных с ошибками в отдельный  словарь
    def log_error(self, data_valid, id_obj):
        self.log_err.setdefault(id_obj, data_valid)

    # забираем товар со склада - id товара и количество
    def take_from_wh(self, id_obj, prod_take_count, division_name=''):
        # получаем группу по id
        group_name = self.id_group.get(id_obj)
        if group_name is None:
            return None
        prod_take_count_in = prod_take_count * 1
        # получаем данные по позиции
        data_obj = self.war_house.get(group_name).get(id_obj)
        product_balance = data_obj[2]
        if 0 < product_balance <= prod_take_count:
            prod_take_count = product_balance
            print(f'Объектов с ID {id_obj} на складе осталось всего {product_balance}, '
                  f'поэтому количество {prod_take_count_in} '
                  f'в заявке было изменено на {product_balance}')
        elif product_balance == 0:
            print(f'Объекты с ID {id_obj} в количестве {prod_take_count_in} отсутствует на складе.')

        product_balance -= prod_take_count
        data_obj[2] = product_balance
        # отправляем данные по данному оборудования в дивизион
        data_obj_to_div = data_obj.copy()
        data_obj_to_div[2] = prod_take_count
        MyDivisions.equipment_add(division_name, (id_obj, data_obj_to_div))
        return prod_take_count  # количесто объектов, которые были взяты со склада

    # полное удаление группы объектов из словаря
    def del_group(self, group_name):
        self.war_house.pop(group_name)

    # удаление объектов со всеми данными по id (группы сохраняются)
    def del_id(self, *args):
        for id_obj in args:
            # получаем группу по id
            group_name = self.id_group.get(id_obj)
            # удаляем данные по id
            if group_name is not None:
                self.war_house.get(group_name).pop(id_obj)
                self.id_group.pop(id_obj)  # подчищаем справочник от удаленного id

    @property
    def show_summary(self):
        # посчитаем количество объектов по группам и стоимость
        summary_result = []
        for key_group, objects in self.war_house.items():
            obj_count = 0
            group_price = 0
            for obj in objects.values():
                obj_count += obj[2]
                group_price += obj[3] * obj_count
            summary_result.append((key_group, obj_count, group_price))
        return summary_result

    @property
    def show_log(self):
        return self.log_err

    def show_info_id(self, search_id):
        try:
            group = self.id_group.get(search_id)
            info_id = self.war_house.get(group).get(search_id)
            if group == 'Printer':
                _obj_show = Printer(*info_id)
            elif group == 'Scaner':
                _obj_show = Scaner(*info_id)
            elif group == 'Xerox':
                _obj_show = Xerox(*info_id)
            return "\n".join(map(lambda x: x.strip(), str(_obj_show).split(',')))
        except:
            return f'не найден на складе'


class Divisions:
    def __init__(self, *args):
        self.names_div = list(args)
        self.eqip_in_div = {}

    def equipment_add(self, name_div, equipment):
        self.eqip_in_div.setdefault(name_div, {})
        group_in_div = self.eqip_in_div.get(name_div)
        if group_in_div.get(equipment[0]) is None:
            group_in_div[equipment[0]] = equipment[1]
        else:
            add_count = group_in_div.get(equipment[0])
            add_count[2] += equipment[1][2]

    @property
    def show(self):
        return self.eqip_in_div


class Equipment(ABC):
    def __init__(self, name, model, count, price, *args):
        self.name = name
        self.model = model
        self.count = count
        self.price = price
        self.other = args
        self.group_name = self.__class__.__name__

    @property
    def name_obj(self):
        return self.group_name

    @abstractmethod
    def all_data(self):
        pass


class Printer(Equipment):
    def __init__(self, name, model, count, price, color, print_speed):
        super().__init__(name, model, count, price)
        self.color = color
        self.print_speed = print_speed

    def __str__(self):
        return f'Марка: {self.name}, Модель: {self.model}, Количество: {self.count}, Стоимость единицы:{self.price}, ' \
               f'Цветная печать: {self.color}, Скорость печати: {self.print_speed}'

    def all_data(self):
        return [self.name, self.model, self.count, self.price, self.color, self.print_speed]


class Scaner(Equipment):
    def __init__(self, name, model, count, price, format_scan='A4', dpi=300):
        super().__init__(name, model, count, price)
        self.format_scan = format_scan
        self.dpi = dpi

    def __str__(self):
        return f'Марка: {self.name}, Модель: {self.model}, Количество: {self.count}, Стоимость единицы:{self.price}, ' \
               f'Формат: {self.format_scan}, Разрешение dpi: {self.dpi}'

    def all_data(self):
        return [self.name, self.model, self.count, self.price, self.format_scan, self.dpi]


class Xerox(Equipment):
    def __init__(self, name, model, count, price, format_xer='A4', dpi=300, mfu=False):
        super().__init__(name, model, count, price)
        self.format = format_xer
        self.dpi = dpi
        self.mfu = mfu

    def __str__(self):
        return f'Марка: {self.name}, Модель: {self.model}, Количество: {self.count}, Стоимость единицы:{self.price}, ' \
               f'Формат: {self.format}, Разрешение dpi: {self.dpi}, МФУ:{self.mfu}'

    def all_data(self):
        return [self.name, self.model, self.count, self.price, self.format, self.dpi, self.mfu]


# ---- Работаем с данными
# -- Проверим работу основных методов на готовых данных

# 1. ------------ Передадим технику на склад -----------------------------
MyWarehouse = Warehouse()
MyDivisions = Divisions('Бухгалтерия', 'Юристы', 'Производство')

# Завозим технику на склад
# считаем, что факту поставки конкретной партии должен быть присвоен ID
obj_1 = Printer('HP', '1020', '20s', 6500, True, 30)  # эти данные с ошибкой в количестве
obj_2 = Printer('CANON', '3050', 21, 5000, True, 25)
obj_3 = Printer('SAMSUNG', '5000', 30, 15000, False, 40)
MyWarehouse.send_to_wh(obj_1)
MyWarehouse.send_to_wh(obj_2)
MyWarehouse.send_to_wh(obj_3)

obj_1 = Scaner('HP', 'ScanJet 970', 10, 3200, 'A4', 300)
obj_2 = Scaner('Epson', '3050', 21, 2800, 'А3', 600)
obj_3 = Scaner('HP', 'Z-500', '15cz', 4200, 'А4', 600)
MyWarehouse.send_to_wh(obj_1)
MyWarehouse.send_to_wh(obj_2)
MyWarehouse.send_to_wh(obj_3)

obj_1 = Xerox('HP', '5035', 5, '25000 долл.', 'A4', 300, True)
obj_2 = Xerox('Canon', '7012', 3, 2800, 'А3', 600, True)
obj_3 = Xerox('Canon', '3012', 4, 4200, 'А3', 600, True)
MyWarehouse.send_to_wh(obj_1)
MyWarehouse.send_to_wh(obj_2)
MyWarehouse.send_to_wh(obj_3)

print("1) --- Оргтехника, которая поступила на склад до распределения:")
pprint(MyWarehouse.war_house)

print('\n Остатки на складе:', MyWarehouse.show_summary)

print('\n Ошибки ввода:')
if len(MyWarehouse.show_log):
    pprint(MyWarehouse.show_log)
else:
    print('без ошибок')


# 2. ------------ Передадим технику со склада в дивизионы -----------------------------
# Забираем оргтехнику со склада в дивизионы - вводим id нужной оргтехники, количество, наименование дивизиона
print('\n2) --- Передача техники в дивизионы:\n')
MyWarehouse.take_from_wh(2, 5, 'Бухгалтерия')
MyWarehouse.take_from_wh(1, 4, 'Юристы')
MyWarehouse.take_from_wh(1, 2, 'Производство')
MyWarehouse.take_from_wh(2, 2, 'Бухгалтерия')
MyWarehouse.take_from_wh(1, 2, 'Юристы')
MyWarehouse.take_from_wh(1, 2, 'Юристы')
MyWarehouse.take_from_wh(1, 2, 'Бухгалтерия')
MyWarehouse.take_from_wh(4, 5, 'Бухгалтерия')
MyWarehouse.take_from_wh(4, 4, 'Юристы')
MyWarehouse.take_from_wh(4, 2, 'Производство')
MyWarehouse.take_from_wh(5, 2, 'Бухгалтерия')
MyWarehouse.take_from_wh(6, 2, 'Юристы')
MyWarehouse.take_from_wh(5, 2, 'Бухгалтерия')
MyWarehouse.take_from_wh(7, 1, 'Бухгалтерия')
MyWarehouse.take_from_wh(8, 10, 'Юристы')
MyWarehouse.take_from_wh(9, 2, 'Бухгалтерия')
MyWarehouse.take_from_wh(8, 5, 'Юристы')  # проверка ситуации, когда оборудование закончилось на складе
pprint(MyDivisions.show)

# 3. ------------ Посмотрим остатки на складе после распределения -----------------------------
print("\n3) --- Оргтехника на складе после распределения:\n")
pprint(MyWarehouse.war_house)
print('\n Остатки на складе:', MyWarehouse.show_summary)

# 4. ------------ Удаляем группу объектов -----------------------------
print("\n4) --- Склад после удаления группы Printer:\n")
MyWarehouse.del_group('Printer')
pprint(MyWarehouse.war_house)

# 5. ------------ Удаляем отедльные объекты -----------------------------
# Удаляем объекты по ID
print("\n5) --- Склад после удаления объектов с id 5 и 8:\n")
MyWarehouse.del_id(5, 8)
pprint(MyWarehouse.war_house)

# 6. --------------Пример вывода информации об объекте по ID
print("\n6) --- Пример вывода информации по ID объекта:")
search_id = 7
print(f'\nДанные по объекту с ID {search_id}:\n'
      f'{MyWarehouse.show_info_id(search_id)}')

search_id = 2
print(f'\nДанные по объекту с ID {search_id}:\n'
      f'{MyWarehouse.show_info_id(search_id)}')

search_id = 9
print(f'\nДанные по объекту с ID {search_id}:\n'
      f'{MyWarehouse.show_info_id(search_id)}')
