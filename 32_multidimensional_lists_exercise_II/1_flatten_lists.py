flatten_matrix = [row.split() for row in input().split('|')]

for row in range(len(flatten_matrix)-1, 0-1, -1):
    if flatten_matrix[row]:
        print(*flatten_matrix[row], end=' ')