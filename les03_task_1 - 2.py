#  Словарь будем хранить в глобальной переменной
DICT_ENG_RU = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}
# --------------- Функция 1. Ищем слово в словаре "как есть"


def num_translate(num_eng):
    """ Если слово не будет найдено, то вернет None.
     Регистр букв не учитывает!"""

    return DICT_ENG_RU.get(num_eng)


# --------------- Функция 2. Перевод с учетом регистра первой буквы


def num_translate_adv(num_eng):
    """ Более универсальный способ перевода"""

    if num_eng.istitle():
        return DICT_ENG_RU.get(num_eng.lower()).title()
    else:
        return DICT_ENG_RU.get(num_eng)


# Запрос данных у пользователя
# print(num_translate(input("Введите числительное от 1 до 10 на английском языке: ")))
user_word = input("Введите числительное от 1 до 10 на английском языке: ")
print(num_translate(user_word))
print(num_translate_adv(user_word))
