class Stationery:
    def __init__(self):
        self.title = 'Канцелярская принадлежность'

    def draw(self):
        return 'запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return 'ручка'


class Pencil(Stationery):
    def draw(self):
        return 'карандаш'


class Handle(Stationery):
    def draw(self):
        return 'маркер'


# Родительский класс
s = Stationery()
print(s.draw())

# Дочерние классы
print('------ ')
pen = Pen()
print(pen.title, '-', pen.draw())

pencil = Pencil()
print(pencil.title, '-', pencil.draw())

handle = Handle()
print(handle.title, '-', handle.draw())

