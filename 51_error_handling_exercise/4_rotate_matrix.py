from custom_exceptions import MatrixContentError, MatrixSizeError


def rotate_matrix(matrix):
    matrix_length = len(matrix)

    for i in range(matrix_length):
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_length):
        matrix[i].reverse()



mtrx = []

while True:
    line = input().split()
    if not line:
        break

    try:
        int_line = list(map(int, line))
    except ValueError:
        raise MatrixContentError('The matrix must consist of only integers')
    else:
        mtrx.append(int_line)

mtrx_length = len(mtrx)

for row in mtrx:
    row_length = len(row)
    if row_length != mtrx_length:
        raise MatrixSizeError('The size of the matrix is not a perfect square')


rotate_matrix(mtrx)

for row in mtrx:
    print(*row, sep=' ')