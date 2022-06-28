# Задача №2 предполгает создание нового списка
# Задаем сообщение в списке
message_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_message_list = list()

# Формируем новый список с форматированием по заданию
for index_in_list, val in enumerate(message_list):
    # print(index_in_list, val.isdigit())
    sign = ''  # тут будем хранить знак числа, если он есть в val
    if "+" in val or "-" in val:  # если есть +-, то запомним его и удалим из val (можно на find() переделать)
        sign = val[0]  # запоминаем знак числа - символ с 0-м индексом
        val = val.replace(sign, '')
    if val.isdigit():
        # форматируем число по условию и делаем распаковку в список с кавычками
        # реализовал вариант без insert()
        dig_format = ['"', f'{sign}{int(val):02d}', '"']
        new_message_list.extend(dig_format)
    else:
        new_message_list.append(message_list[index_in_list])
# выводим новый список
print(new_message_list)

# Формируем строку по  - нужно убрать пробел у кавычки с нужной стороны
# Предположим, что если в списке попадается открыв. кавычка, то пробелы не добавляются до закрывающей
status_quote = False  # в переменной храним факт того, что нашли кавычку
for show_val in new_message_list:
    if (show_val != '"' and not status_quote) or (show_val == '"' and status_quote):
        # если текущий символ не кавычка и мы не находимся внутри кавычек
        status_quote = False
        print(show_val, end=' ')
    elif show_val == '"' and not status_quote:
        status_quote = True  # т.е. попадаем в поле с кавычкой и не делаем после нее пробел
        print(show_val, end='')
    else:
        print(show_val, end='')
