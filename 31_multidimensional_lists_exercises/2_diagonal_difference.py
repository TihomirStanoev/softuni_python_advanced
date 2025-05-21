matrix = [[int(x) for x in input().split()]for row in range(int(input()))]


primary_diagonal = sum(matrix[i][i] for i in range(len(matrix)))
secondary_diagonal = sum(matrix[i][-i-1]for i in range(len(matrix)))

print(abs(primary_diagonal-secondary_diagonal))