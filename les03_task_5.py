from random import choice, randrange

NOUNS = ["автомобиль", "лес", "огонь", "город", "дом"]
ADVERBS = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
ADJECTIVES = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


# --------------- 5.1. Реализация основного условия задачи


def get_jokes(n):
    """Function return jokes

        Keyword arguments:
        n - count jokes gen.

        """
    jokes_list = []
    # jokes_list.append(" ".join([choice(NOUNS), choice(ADVERBS), choice(ADJECTIVES)]))
    for i in range(n):
        jokes_list.append(" ".join([choice(NOUNS), choice(ADVERBS), choice(ADJECTIVES)]))
    return jokes_list


print("1. Результат работы функции по основному условию: ", get_jokes(2))



# ----------------- 5.2. Функция с возможностью получения шуток без повторов

# функция возвращает рандомную позицию удаляемого эл.


def p_index(x_list):
    return randrange(0, len(x_list))

# Вариант с lambda не проходит проверку по PEP8. Почему не понял??
# p_index = lambda x_list: randrange(0, len(x_list))

# Основная функция


def get_jokes_adv(n, unique_check=True):
    """Function return jokes

        Keyword arguments:
        n - count jokes gen.
        unique_check - unique words (default - True)

        """
    # сделал копию списков, чтобы исходные не трогать
    nouns_copy = NOUNS.copy()
    adverbs_copy = ADVERBS.copy()
    adjectives_copy = ADJECTIVES.copy()
    jokes_list = []
    for i in range(n):
        if unique_check:
            jokes_list.append(" ".join([nouns_copy.pop(p_index(nouns_copy)),
                                        adverbs_copy.pop(p_index(adverbs_copy)),
                                        adjectives_copy.pop(p_index(adjectives_copy))]))
        else:
            jokes_list.append(" ".join([choice(nouns_copy), choice(adverbs_copy), choice(adjectives_copy)]))
    return jokes_list


print("2A. Результат по дополнительному условию без флага (есть повторы): ", get_jokes_adv(5, unique_check=False))
print("2B. Результат по дополнительному условию с флагом (уникальные): ", get_jokes_adv(5, unique_check=True))
