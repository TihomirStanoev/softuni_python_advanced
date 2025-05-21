matrix = [[int(x) for x in input().split(', ')]for row in range(int(input()))]


primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
secondary_diagonal = [matrix[i][-i-1]for i in range(len(matrix))]

print(f"Primary diagonal: {', '.join(str(num) for num in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(num) for num in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")