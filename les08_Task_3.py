from functools import wraps

# Выполнены следующие условия задачи:
    # несколько аргументов через запятую;
    # выводится тип значения функции;
    # добавлена возможность использования именованного аргумента - выводит имя функции на True;
    # замаскирована работа декоратора.


def arg_type_logger(show_function=False):
    def type_logger(func):
        @wraps(func)
        def answer(*args, **kwargs):
            if show_function:
                result_list = [f'{func.__name__}({i}: {type(i)})' for i in args]
            else:
                result_list = [f'{i}: {type(i)}' for i in args]
            print(*result_list, sep=', ')
            # Добавлен вывод результатов расчета
            result_func = [func(i) if isinstance(i, int) or isinstance(i, float)
                           else f'*** Функция не применима для "{i}"  - {type(i)} ***' for i in args]
            print('Результаты расчета:', ', '.join(map(str, result_func)))
            return result_list
        return answer
    return type_logger


# @type_logger
# show_function=True --> calc_cube(5: <class 'int'>)
# show_function=False --> 5: <class 'int'>
@arg_type_logger(show_function=True)
def calc_cube(x):
    return x ** 3

# Результаты:

# --- 1. Базовое условие
a = calc_cube(5)
# print(*a)
# 5: <class 'int'>
# print(calc_cube)  # <function calc_cube at 0x00000229034FFEE0> - результат маскировки


# ---- 2. Расширенный вариант
a = calc_cube(5, 6.5, '7а', [1, 2])
# 5: <class 'int'>, 6: <class 'int'>, 7а: <class 'str'>, [1, 2]: <class 'list'>

