def create_matrix(r):
    return [[int(x) for x in input().split()] for i in range(r)]

n = int(input())

matrix = create_matrix(n)

diagonal_sum = sum(matrix[index][index] for index in range(n))

print(diagonal_sum)