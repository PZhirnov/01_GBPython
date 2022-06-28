# ---------------------------- Задача №4


def thesaurus_adv(names_in_func, sort_status=False):
    name = list(map(lambda x: [x.split()[0][0], x.split()[0]], names_in_func))
    last_name = list(map(lambda x: [x.split()[1][0], x.split()[1]], names_in_func))
    names_and_last_names = list(zip(name,  last_name))
    # данные будут отсортированы перед обработкой по двум ключам - 1 - фамилия, 2 - имя
    if sort_status:
        names_and_last_names.sort(key=lambda x_list: (x_list[1][1], x_list[0][1]))
    dict_res = {}
    for name_in, last_name_in in names_and_last_names:
        full_name = f'{name_in[1]} {last_name_in[1]}'
        if dict_res.get(last_name_in[0]) is None:
            dict_res.update({last_name_in[0]: {name_in[0]: [full_name]}})
        else:
            if dict_res.get(last_name_in[0]).get(name_in[0]) is None:
                dict_res.get(last_name_in[0]).update({name_in[0]: [full_name]})
            else:
                dict_res.get(last_name_in[0]).get(name_in[0]).append(full_name)
                dict_res.get(last_name_in[0]).get(name_in[0]).sort()
    return dict_res


# Исходные данные:
names = ["Иван Сергеев", "Инна Серова",
         "Петр Алексеев", "Илья Иванов",
         "Анна Савельева", "Харитон Сергеев",
         "Харитон Юдин", "Павел Жирнов",
         "Глеб Жиглов"
         ]
# без сортировки
print('1. Вывод данных без сортировки - как в условии:')
print(thesaurus_adv(names), "\n")
# с сортировкой
print('2. Вывод данных с сортировкой по двум ключам (фамилия - имя):')
print(thesaurus_adv(names, True))
