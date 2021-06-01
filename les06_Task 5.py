from sys import argv
# Задание №5. Делаем запись в файл + аргументы в командной строке
# python "les06_Task 5.py" users_hobby.txt users.csv hobby.csv
hobby_lines = ''
with open(argv[1], 'w', encoding='utf-8') as f_result:
    with open(argv[2], 'r', encoding='utf-8') as f_users:
        with open(argv[3], 'r', encoding='utf-8') as f_hobby:
            for lines_user in f_users:
                hobby_lines = f_hobby.readline().strip()
                user_hobby = f'{lines_user.strip()}: {hobby_lines if hobby_lines != "" else None}\n'
                f_result.write(user_hobby)
