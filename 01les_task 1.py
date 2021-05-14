# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах.
# для проверки:  180500  -- > 2 дн. 2 час. 8 мин. 20 сек.
duration_sec = int(input('Введите продолжительность периода в секундах:'))

# посчитаем целое значение всех возможных единиц для указанной продолжительности в секундах
seconds = duration_sec % 60
minutes = duration_sec // 60
hours = minutes // 60
days = hours // 24
months = days // 30
years = months // 12

# находим остаток от деления для каждой единицы временного интервала
# seconds и years уже посчитаны
minutes = minutes % 60
hours = hours % 24
days = days % 30
months = months % 12

# 1-й вариант вывода результата (все сразу)
print('Вариант 1. Все выводим разом')
print(f'{years} г. {months} мес. {days} дн. {hours} час. {minutes} мин. {seconds} сек.')

print('\n', '-' * 100)  # разделить для улучшения восприятия результатов

# 2-й вариант вывода результата с пропуском 0-х показателей
print('Вриант 2. Выводим все без нулевых')
time_duration = [years, months, days, hours, minutes, seconds]  # сделал так, но можно сразу добавить именя периодов
time_label = ['г.', 'мес.', 'дн.', 'час.', 'мин.', 'сек.']
for val in range(len(time_duration)):
    if time_duration[val] != 0:
        print(time_duration[val], time_label[val], end=' ')
print('\n', '-' * 100)

# 3-й вариант вывода результата (использует список из 2-го)
print('\nВариант 3. Выводим все с первого не пустого (как в задаче).')
start_pos = False  # если найдено первое не нулевое, то ставим True
for val in range(len(time_duration)):
    if time_duration[val] != 0:
        start_pos = True
    if start_pos:
        print(time_duration[val], time_label[val], end=' ')
