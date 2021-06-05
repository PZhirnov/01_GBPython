import yaml
from os.path import exists, join
from os import mkdir


def create_all(dict_in, start_path=''):
    for key_folder, all_in_folder in dict_in.items():
        full_path_key_folder = join(start_path, key_folder)
        if not exists(full_path_key_folder):
            mkdir(full_path_key_folder)
            print("Создана папка: ", join(start_path, key_folder))
        else:
            print("Каталог ", join(start_path, key_folder), " создан ранее!")
        if isinstance(all_in_folder, dict):
            recursion = create_all(all_in_folder, full_path_key_folder)
        if isinstance(all_in_folder, list):
            for i in all_in_folder:
                # Если объект в словаре не каталог, то создаем файл
                if not isinstance(i, dict):
                    name_file = join(full_path_key_folder, i)

                    if not exists(name_file):
                        print('+ файл', name_file)
                        with open(name_file, 'w', encoding='utf-8') as f:
                            f.write('')
                    else:
                        print('Файл', name_file, 'уже существует!')
                elif isinstance(i, dict):
                    recursion = create_all(i, full_path_key_folder)
                else:
                    print('Неизвествне данные:', i)  # чтобы не потерять что-либо, если будет
    return True


# Читаем данные из файла
with open('config.yaml', 'r', encoding='utf-8') as f:
    result = yaml.safe_load(f)
# Запускаем функцию
print('Работа заершена без ошибок!' if create_all(result) is True
      else 'Работа завершена с ошибками!')
