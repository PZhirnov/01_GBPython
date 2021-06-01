import json

# Формаируем словарь по условию
with open('users.csv', 'r', encoding='utf-8') as f_users:
    with open('hobby.csv', 'r', encoding='utf-8') as f_hobby:
        dict_users = {}
        for lines_user in f_users:
            hobby_lines = f_hobby.readline().strip()
            dict_users[lines_user.strip()] = hobby_lines if hobby_lines != '' else None
        # проверяем остаток данных в файле хобби - для проверки необходимости вывода exit(1)
        remains_hobbys = sum(rem_line_hobbys.count('\n') for rem_line_hobbys in iter(lambda: f_hobby.readline(), ''))

# Выводим полученный словарь
print(dict_users)

# Сохранение словаря в json
with open('save_res.json', 'w', encoding='utf-8') as f:
    json.dump(dict_users, f)

# Сохранение в текстовом формате
with open('save_res.csv', 'w', encoding='utf-8') as f:
    for user, hobby in dict_users.items():
        f.writelines([user, f': {hobby}\n'])

exit(1) if remains_hobbys > 0 else None
