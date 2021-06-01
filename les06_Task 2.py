# -------- Задание №2. Ищем спамера.
# Создаем словарь с уникальными IP, где ставим счетчики
print(f"{'-'*25} Задание 2 {'-'*100}")
dict_ip = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.split()
        ip = line[0]
        if dict_ip.get(ip):
            dict_ip[ip] += 1
        else:
            dict_ip[ip] = 1

tuple_dic = tuple(dict_ip.items())
print("IP главного спамера: {}  Количество запросов: {}".format(*max(tuple_dic, key=lambda x: x[1])))
