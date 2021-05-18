# Задание №5.
# Исходные данные: список цен на товары

price_list = [57.8, 46.51, 97, 200.93, 5.64, 500, 20.8, 17.5,
              12.6, 50.5, 35.12, 12.5, 14.30, 30.10, 20, 20.21,
              1000.54, 100.25, 3.15, 15.20]

# --- А. Вывод цен в одну строку
print(f'{"-"*20} Задание А {"-"*20}\n')
# Решение:
for num, price in enumerate(price_list):
    rub = int(price)
    cent = round(price % 1 * 100)  # так копейки будут корректно возвращаться в любом случае
    print(f'{num + 1}) {rub:2d} руб. {cent:02d} коп.', end=' ')
print('\n')


# --- B. Вывести цены отсортированные по возрастанию и доказать, что объект списка тот же.
print(f'{"-"*20} Задание B {"-"*20}\n')
# Решение:
id_in = id(price_list)  # запоминаем id исходного списка
price_list.sort()
id_out = id(price_list)  # проверяем id после сортировки
print(f'id списка до сортировки: {id_in}\n'
      f'id спика после сортировки: {id_out}\n'
      f'Результат сравнения: {id_in == id_out}'
      )
# Выведем решение B
for num, price in enumerate(price_list):
    rub = int(price)
    cent = round(price % 1 * 100)
    print(f'{num + 1}) {rub:2d} руб. {cent:02d} коп.', end=' ')
print('\n')


# --- C. Создать новый список, содержащий те же цены, но отсортированные по убыванию
print(f'{"-"*20} Задание С {"-"*20}\n')
# Решение:
price_list_new = sorted(price_list, reverse=True)
print('Создан новый список, но отсортированный по убыванию - id списка:', id(price_list_new))
print(price_list_new)
# Выведем решение С
for num, price in enumerate(price_list_new):
    rub = int(price)
    cent = round(price % 1 * 100)
    print(f'{num + 1}) {rub:2d} руб. {cent:02d} коп.', end=' ')
print('\n')


# --- D. Вывести цены пяти самых дорогих товаров.
# Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
print(f'{"-"*20} Задание D {"-"*20}\n')
# D.1 Решение на базе того, что сделано выше
print("Вариант 1: ", end='')
for num, price in enumerate(price_list_new[:5:1]):
    print(f'{num + 1}) {int(price):2d} руб. {round(price % 1 * 100):02d} коп.',
          end=', ')  # все в одной строке
print('\n')

# Решение с помощью map в одну строку - для собственной тренировки
print("Вариант 2. Решение в одну строку, но с map: ", end='')
print(", ".join(list(map(
    lambda price_in: f'{int(price_in):2d} руб. '
                     f'{round(price_in % 1 * 100):02d} коп.',
    price_list_new[:5:1]))))
