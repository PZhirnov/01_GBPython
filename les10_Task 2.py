from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param
        self.material = 0

    @abstractmethod
    def material_consumption(self):
        pass

    @property
    def consumption(self):
        return self.material_consumption()


class Coat(Clothes):
    def material_consumption(self):
        res_consum = self.param/6.5 + 0.5
        return res_consum


class Suit(Clothes):
    def material_consumption(self):
        res_consum = 2 * self.param + 0.3
        return res_consum


coat = Coat(60)
# print(coat.material_consumption())  -  # 9.73
print(f'На пальто нужно {coat.consumption:0.2f} ')
suit = Suit(5)
print(f'На костюм нужно {suit.consumption:0.2f} ')
print(f'Итого: {coat.consumption + suit.consumption:0.2f}')
