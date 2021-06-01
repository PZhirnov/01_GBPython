from sys import argv

if len(argv) == 1:
    print('Вы не ввели параметр!')
    exit()

with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.writelines(f'{argv[1].strip():7.7}\n')
