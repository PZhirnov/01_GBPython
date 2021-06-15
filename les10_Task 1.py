class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "\n".join(map(lambda x: "\t".join(map(str, x)), self.matrix))

    def __add__(self, other):
        # складывать допускается только матрицы одинаковой размерности (m х n)
        result_matrix = []
        m, n = len(self.matrix), len(self.matrix[0])
        if m == len(other.matrix) and n == len(other.matrix[0]):
            for m in range(m):
                row_val = []
                for i in range(n):
                    row_val.append(self.matrix[m][i] + other.matrix[m][i])
                result_matrix.append(row_val)
        else:
            raise ValueError
        return Matrix(result_matrix)


matrix_1 = Matrix([[311, 22], [37, 43], [51, 86]])
matrix_2 = Matrix([[3, 5], [3, 10], [3, 11]])
matrix_3 = Matrix([[3, 5], [3, 10], [3, 1101]])
print("Матрица 1:\n", matrix_1, sep='')
print("Матрица 2:\n", matrix_2, sep='')
print("Матрица 3:\n", matrix_3, sep='')

try:
    print("Результат сложения:\n", matrix_1 + matrix_2 + matrix_3, sep='')
except ValueError:
    print('Все матрицы должны быть одного размера!')
# print("Результат сложения:\n", matrix_1 + matrix_2, sep='')
# Вывод
# 1 2
# 3 4
# 5 6
