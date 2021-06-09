import re

RE_ALL = re.compile(r'[^\"\s\[\]\-]+')


list_tuple = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        res_parse = re.findall(RE_ALL, line)[:8]
        # Если нужен вывод полностью сопоставимый с заданием, то снять комментирование
        # res_parse.pop(5)
        # merge = res_parse.pop(2)
        # res_parse[1] = f'{res_parse[1]} {merge}'
        print(tuple(res_parse))
