from sys import argv
from itertools import islice


def list_argv(start=None, end=None):
    if end:
        end = int(end)
    if start:
        start = int(start) - 1
    return [start, end]


# list_control = list_argv('3', '4')
list_control = list_argv(*argv[1:])

# Вариант вывода данные с itertools
with open('bakery.csv', 'r', encoding='utf-8') as f:
    result_answ = islice(f, *list_control)
    #  print(type(result_answ))  # <class 'itertools.islice'>
    for i in result_answ:
        print(str(i).strip())
