# --------------- Задание №3 c ZIP
# выглядит лучше и понятнее + сортировка


def thesaurus(names_in):
    key_name_list = list(sorted(zip(list(map(lambda x: x[0], names_in)), names_in)))
    dict_res = {}
    for key_in, name_in in key_name_list:
        if dict_res.get(key_in) is None:
            dict_res.update(zip([key_in], [[name_in]]))
        else:
            dict_res.get(key_in).append(name_in)
            dict_res.get(key_in).sort()
    return dict_res

names_list = ["Иван", "Мария", "Петр", "Илья", "Алена", "Христофор", "Аня", "Харитон"]
print("Исходный список: \n", names_list)
print("Результат работы функции: \n", thesaurus(names_list))
