# создается потомок класса Exception
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    a, b = input('Введите числитель a и знаменатель b: ').split()
    try:
        a, b = float(a), float(b)
        if b == 0:
            raise OwnError('В знаменателе не может быть 0!')
    except OwnError as err:
        print(err)
    except ValueError:
        print('Вы ввели не число!')
    else:
        print(f'Результат деления: {a/b:.2f}')
