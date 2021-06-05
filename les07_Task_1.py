import os
# 1. Имя объекта зранится в ключах, а содержимое в значениях.
# 2. Если значение словарь, то смотрим его, а если None или пустой словарь, то значит пустая папка
# 3. Все остальные случаи предполагают создание файла с именем по ключу и содержимым по значению.


def start_dir_create(dict_folders_in, path_start=''):
    """
    Создает каталог папок и файлов по описанию конфигурации из словаря.
    Существующие файлы и папки не перезаписываются.
    Каталог может быть создан в нужно директории - второй параметр.
    :return: список c данными [созданных папок, созданных файлов]
    """
    stat_after_create = [0, 0]  # после работы функции вернем статистику 0 - новых папок, 1 - новых файлов
    for parent_obj, child_obj in dict_folders_in.items():
        if path_start != "":
            cur_obj = f"{path_start}\\{parent_obj}"
        else:
            cur_obj = parent_obj
        # если значение по ключу словарь, то смотрим на его содержимое
        if isinstance(child_obj, dict):
            # создаем новый каталог и заходим в него поработать
            if not os.path.exists(cur_obj):
                os.mkdir(cur_obj)
                stat_after_create[0] += 1
            stat_add = start_dir_create(child_obj, cur_obj)
            stat_after_create[1] += stat_add[1]
            stat_after_create[0] += stat_add[0]
        elif child_obj is None:
            path_dir_create = cur_obj
            if not os.path.exists(path_dir_create):
                os.mkdir(path_dir_create)
                stat_after_create[0] += 1

        else:
            # создаем файл, если это не каталог
            if not os.path.exists(cur_obj):
                with open(cur_obj, 'w', encoding='utf-8') as f:
                    f.write(child_obj)
                    stat_after_create[1] += 1
    return stat_after_create


# ------ Настраиваемая конфигурация каталога в словаре
# если папка пустая, то можно значение поставить None или пустой словарь {}
struct_desc = {
    "my_project_task_1": {
        "settings": None,
        "mainapp": None,
        "adminapp": None,
        "authapp": {
            "myidea.txt": "work it easy!",
            "myresult.txt": "every day!",
            "newauth": {}
            },
        "index.html": "Hello world!",
        "config.sys": "start = 2021"
        }
    }

stat_result = start_dir_create(struct_desc)
print("Создано {} папок и {} файла.".format(*stat_result))
