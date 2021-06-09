from functools import wraps


def val_checker(check):
    def type_logger(func):
        @wraps(func)
        def answer(*args, **kwargs):
            if not (False in [check(i) for i in args]):
                result_list = [f'{func.__name__}({i}: {type(i)})' for i in args]
                result_func = [func(i) for i in args if isinstance(i, int)
                               or isinstance(i, float)]
            else:
                msg = f'wrong val {args[0]}'
                raise ValueError(msg)
            print(*result_list, sep=', ')
            print('Результаты расчета:', ', '.join(map(str, result_func)))
            return result_list
        return answer
    return type_logger


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

# Результаты:

# --- 1. Базовое условие c одним значением
try:
    a = calc_cube(-5)
except ValueError as err:
    print(err)
# print(*a)
# 5: <class 'int'>
# print(calc_cube)  # <function calc_cube at 0x00000229034FFEE0> - результат маскировки


# ---- 2. Расширенный вариант
try:
    a = calc_cube(5, 6, 7)
except ValueError as err:
    print(err)
# 5: <class 'int'>, 6: <class 'int'>, 7: <class 'int'>
# Результаты расчета: 125, 216, 343


# --- 3. Вариант с -5
# a = calc_cube(-5)
#  raise ValueError(msg)
# ValueError: wrong val -5