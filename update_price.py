from sys import argv


# Решение при условии, что максимальный размер поля в базе определен - формат "7777,77"
size_conf = 9  # - 7 символов и \n
# номер записи
num_price, new_val = argv[1:3]
new_val = f'{new_val:7.7}\n'
pos_in_data = size_conf * (int(num_price) - 1)

with open('bakery.csv', 'r+', encoding='utf-8') as f:
    f.seek(pos_in_data)
    if f.readline() != '':
        f.seek(pos_in_data)
        f.write(new_val)
    else:
        print('В указанной позиции нет данных!')
