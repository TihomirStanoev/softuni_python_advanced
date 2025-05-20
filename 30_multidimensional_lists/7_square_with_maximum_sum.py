def create_matrix(r):
    return [[int(number) for number in input().split(', ')] for _ in range(r)]


def matrix_sum(i_matrix):
    return sum(i_matrix[r][c] for c in range(len(i_matrix)) for r in range(len(i_matrix)))


rows, cols = list(map(int, input().split(', ')))

matrix = create_matrix(rows)

max_sum = float('-inf')
max_matrix = []

for row_index in range(rows-1):
    for col_index in range(cols-1):
        inner_matrix = [[matrix[row_index][col_index], matrix[row_index][col_index+1]],
                        [matrix[row_index+1][col_index], matrix[row_index+1][col_index+1]]]

        inner_sum = matrix_sum(inner_matrix)
        if inner_sum > max_sum:
            max_sum = inner_sum
            max_matrix = inner_matrix


first_row, second_row = max_matrix

print(*first_row)
print(*second_row)
print(max_sum)
