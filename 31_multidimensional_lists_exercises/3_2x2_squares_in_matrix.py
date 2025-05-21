def is_found(a,b,c,d):
    return a == b and b == c and c == d and d == a



rows, cols = [int(num) for num in input().split()]

matrix = [input().split() for row in range(rows)]


square_matrices = 0
for row_index in range(rows-1):
    for col_index in range(cols-1):

        top_left, top_right = matrix[row_index][col_index], matrix[row_index][col_index+1]
        bottom_left, bottom_right = matrix[row_index+1][col_index], matrix[row_index+1][col_index+1]

        if is_found(top_left, bottom_left, top_right, bottom_right):
            square_matrices += 1

print(square_matrices)