def create_matrix(r,c):
    return [[int(x) for x in input().split()] for i in range(r)]


matrix = create_matrix(*list(map(int, input().split(', '))))


for col in range(len(matrix[0])):
    col_sum = 0
    for row in range(len(matrix)):
        col_sum += matrix[row][col]
    print(col_sum)
