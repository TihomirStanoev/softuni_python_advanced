matrix = []

for row_i in range(int(input())):
    matrix.extend([int(number) for number in input().split(', ')])

print(matrix)