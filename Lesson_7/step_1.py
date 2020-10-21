from random import randint
from math import ceil


class Matrix:
    x, y = 0, 0
    sum_matrix = []

    def __init__(self, mat):
        self.mat = mat
        if not (Matrix.x and Matrix.y):
            Matrix.x = len(mat)
            Matrix.y = min([len(i) for i in mat])
            for i in range(Matrix.x):
                Matrix.sum_matrix = [[0 for _ in range(Matrix.y)]for _ in range(Matrix.x)]

    def __str__(self):
        return ''.join(['\t'.join(str(i) for i in j) + '\n' for j in self.mat])

    def __add__(self, other):
        if Matrix.sum_matrix == [[0 for _ in range(Matrix.y)]for _ in range(Matrix.x)]:
            for i in range(Matrix.x):
                for j in range(Matrix.y):
                    Matrix.sum_matrix[i][j] = other.mat[i][j] + self.mat[i][j]
            return Matrix([self.mat[i] + [
                '\t' if i + 1 != ceil(self.x / 2) else '  + ']
                           + other.mat[i] + ['\t' if i + 1 != ceil(self.x / 2) else '  = ']
                           + Matrix.sum_matrix[i] for i in range(len(self.mat))])
        else:
            for i in range(Matrix.x):
                for j in range(Matrix.y):
                    Matrix.sum_matrix[i][j] += other.mat[i][j]
            return Matrix([self.mat[i][:len(self.mat[i]) - (len(self.mat[i])) % (Matrix.y + 1) - 1]
                           + ['\t' if i + 1 != ceil(self.x / 2) else '  + ']
                           + other.mat[i] + ['\t' if i + 1 != ceil(self.x / 2) else '  = ']
                           + Matrix.sum_matrix[i] for i in range(len(self.mat))])


matrix1 = Matrix([[randint(-5, 5)for _ in range(4)] for _ in range(5)])
matrix2 = Matrix([[randint(-5, 5)for _ in range(4)] for _ in range(5)])
matrix3 = Matrix([[randint(-5, 5)for _ in range(4)] for _ in range(5)])
matrix4 = Matrix([[randint(-5, 5)for _ in range(4)] for _ in range(5)])

print('Исходные матрицы:')
print(matrix1, matrix2, matrix3, matrix4, sep='\n')

print(matrix1 + matrix2 + matrix3 + matrix4)
