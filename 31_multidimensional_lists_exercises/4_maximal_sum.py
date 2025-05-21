def inner_matrix(r, c, _i):
    return [[matrix[x][y] for y in range(c, c+_i)] for x in range(r, r+_i)]


def matrix_sum(matrix_3x3):
    total = 0
    for row in matrix_3x3:
        total += sum(row)
    return total


rows, cols = [int(num) for num in input().split()]
matrix = [list(map(int, input().split())) for row in range(rows)]
i = 3

small_matrix_sum = -float('inf')
small_matrix = []

for row in range(0, rows - i+1):
    for col in range(0, cols-i+1):
        matrix_in = inner_matrix(row, col, i)
        sum_in = matrix_sum(matrix_in)

        if sum_in > small_matrix_sum:
            small_matrix_sum = sum_in
            small_matrix = matrix_in


print(f"Sum = {small_matrix_sum}")
for row in small_matrix:
    print(*row)