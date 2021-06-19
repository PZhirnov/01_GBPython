# Сделал два варианта  - 1. Расчет по формулам, 2. Расчет с помощью функции complex()

# ---- Вариант с функцией complex
print('----- Вариант 1 -----')


class ComplexNum:

    def __init__(self, val):
        self.a, self.b = list(map(str, val))
        self.a = float(self.a)
        self.b = float(self.b)

    def __str__(self):
        return f'{self.a} + {self.b}i'

    def __add__(self, other):
        return ComplexNum([self.a + other.a,
                           self.b + other.b])

    def __mul__(self, other):
        return ComplexNum([self.a * other.a - self.b * other.b,
                           self.a * other.b + other.a * self.b])


complex_1 = ComplexNum([5, 10])  # передаем число 5 + 10i
complex_2 = ComplexNum([12, 10])
print(complex_1 + complex_2)
print(complex_1 * complex_2)
