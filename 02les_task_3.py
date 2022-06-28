# Задача №3. Не создаем новй список
# Задаем сообщение в списке
message_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(f"id списка до преобразований: {id(message_list)}")
# Формируем новый список с форматированием по заданию
pos_in_list = 0
while pos_in_list <= (len(message_list) - 1):
    val = message_list[pos_in_list]
    sign = ''  # тут будем хранить знак числа, если он есть в val
    if "+" in val or "-" in val:  # если есть +-, то запомним его и удалим из val (можно на find() переделать)
        sign = val[0]  # запоминаем знак числа - символ с 0-м индексом
        val = val.replace(sign, '')
    if val.isdigit():
        # форматируем число по условию и делаем распаковку в список с кавычками
        message_list[pos_in_list] = f'{sign}{int(val):02d}'
        # вставляем кавычки
        message_list.insert(pos_in_list, '"')
        # если последнее значение списке число, то ошибки не будет
        message_list.insert(pos_in_list + 2, '"')
        pos_in_list += 1  # делаем тут смещение на +1, чтобы уйти в нужную позицию
    else:
        pass
    pos_in_list += 1  # переходим на следующую позицию
# выводим новый список
print(message_list)
# Формируем строку по  - нужно убрать пробел у кавычки с нужной стороны
# Предположим, что если в списке попадается открыв. кавычка, то пробелы не добавляются до закрывающей
status_quote = False  # в переменной храним факт того, что нашли кавычку
for show_val in message_list:
    if (show_val != '"' and not status_quote) or (show_val == '"' and status_quote):
        # если текущий символ не кавычка и мы не находимся внутри кавычек
        status_quote = False
        print(show_val, end=' ')
    elif show_val == '"' and not status_quote:
        status_quote = True  # т.е. попадаем в поле с кавычкой и не делаем после нее пробел
        print(show_val, end='')
    else:
        print(show_val, end='')
# проверяем факт того, что работали с исходным списком
print(f"\nid списка после преобразований: {id(message_list)}")
