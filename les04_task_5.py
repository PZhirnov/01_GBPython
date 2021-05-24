import utils as ut
from sys import argv

# Проверим наличие введенных данных
if len(argv) > 1:
    cur_input = argv[-1]
    print(f"Курс {str(cur_input).upper()}: {ut.currency_rates(cur_input)[0]} "
          f"за {ut.currency_rates(cur_input )[1]} ед., {ut.date_cur()}")
else:
    print("Вы не ввели параметр - USD, EUR и т.д.!")
