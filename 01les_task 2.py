# Объявляем переменные
list_cub = list()
res_sum_one = 0
res_sum_two = 0

# 1. Создаем списко по условию и вычисляем сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7
for val in range(1, 1000, 2):
    # добавляем значения в список
    val_in_list = val**3
    list_cub.append(val_in_list)
    # суммируем цифры числа
    digit = val_in_list
    sum_digits = 0
    while digit != 0:
        sum_digits += digit % 10
        digit = digit // 10
    # проверяем выполнение условия - число должно делиться нацело на 7
    if sum_digits % 7 == 0:
        res_sum_one += val_in_list
# print(list_cub)   # выведем просто для проверки
print('Сумма чисел из списка, сумма цифр которых делится нацело на 7, будет равна: ', res_sum_one)

# 2. К каждому элементу списка добавить 17 и заново вычислить сумму
# тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Внимание: новый список не создавать!!! - Ok
for index_list in range(len(list_cub)):
    list_cub[index_list] += 17
    # выполняем повторно суммирование и проверяем результат
    val_in_list = list_cub[index_list]
    digit = val_in_list
    sum_digits = 0
    # суммируем цифры числа
    while digit != 0:
        sum_digits += digit % 10
        digit = digit // 10
    # проверяем условие
    if sum_digits % 7 == 0:
        res_sum_two += val_in_list
#  print(list_cub)   # выведем просто для проверки
print('Сумма чисел из списка после добавления 17, сумма цифр которых делится нацело на 7, будет равна: ', res_sum_two)
