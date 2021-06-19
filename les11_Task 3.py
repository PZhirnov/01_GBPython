list_val = []


class OwnError(Exception):
    def __init__(self, num):
        self.num = num
        try:
            list_val.append(float(num))
        except:
            print("Вы ввели не число!")


while True:
    num = input('Введите число для добавления в список: ')
    try:
        raise OwnError(num)
    except OwnError as err:
        if str(err) == 'stop':
            break
# Выводим результат
print(list_val)
