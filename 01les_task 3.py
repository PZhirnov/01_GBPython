# Реализовать склонение слова «процент» для чисел до 20.
# Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента».
# Вывести все склонения для проверки.
input_percent = 20
dec_word_percent = ''
for percent_val in range(input_percent + 1):
    rem_val = percent_val % 10
    if rem_val == 1 and percent_val != 11:
        dec_word_percent = "процент"
        # добавил percent_val // 10 != 1, чтобы результат был: 11,12,13,14 процентов.
    elif rem_val < 5 and rem_val != 0 and percent_val // 10 != 1:
        dec_word_percent = "процента"
    else:
        dec_word_percent = "процентов"
    # выводим результаты
    print(f'{percent_val} {dec_word_percent}')
