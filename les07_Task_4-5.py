from os import walk, getcwd
from os.path import join, getsize, splitext
from pprint import pprint
import json


# Путь к текущей папке или указать свою
folder = getcwd()

# Создадим полный реестр файлов из каталога
list_files = []
for root, dirs, files in walk(folder):
    for file in files:
        list_files.append((file, getsize(join(root, file)), splitext(join(root, file))[1]))

# Условия вывода данных
control_range = [0, 100, 1000, 10000, 100000]
res_dict = {}
for num, end_range in enumerate(control_range[1:]):
    start_range = control_range[num]
    list_in_filter = list(filter(lambda size: end_range > size[1] >= start_range, list_files))
    file_ext = [str(ext[2]) for ext in list_in_filter]
    res_dict[end_range] = (len(list_in_filter), list(set(file_ext)))

pprint(res_dict)
fn = folder.split("\\")
with open(f'{fn[-1]}_summary.json', 'w', encoding='utf-8') as f:
    json.dump(res_dict, f)
