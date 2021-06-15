class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return f'{self.cell}'

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        return Cell(self.cell - other.cell) if self.cell > other.cell else 'Разность меньше нуля!'

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __floordiv__(self, other):
        return Cell(self.cell // other.cell)

    def make_order(self, row):
        show_text = '*' * self.cell
        n = int(self.cell / row)
        return [show_text[i:i + n] for i in range(0, len(show_text), n)]


cell_1 = Cell(150)
cell_2 = Cell(25)
print(" __str__ - ", cell_1, " и ",  cell_2)
print(" __add__ - ", cell_1 + cell_2)
print(" __sub__ - ", cell_1 - cell_2)
print(" __mul__ - ", cell_1 * cell_2)
print(" __floordiv__ - ", cell_1 // cell_2)

print("\nВывод с помощью __make_order__:")
print("\n".join(cell_1.make_order(5)))
