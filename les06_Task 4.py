# Задание №4. Делаем сразу запись в файл
hobby_lines = ''
with open('users_hobby.txt', 'w', encoding='utf-8') as f_result:
    with open('users.csv', 'r', encoding='utf-8') as f_users:
        with open('hobby.csv', 'r', encoding='utf-8') as f_hobby:
            for lines_user in f_users:
                hobby_lines = f_hobby.readline().strip()
                user_hobby = f'{lines_user.strip()}: {hobby_lines if hobby_lines != "" else None}\n'
                f_result.write(user_hobby)
