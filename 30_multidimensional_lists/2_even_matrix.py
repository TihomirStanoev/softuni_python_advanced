even_matrix = [[int(number) for number in input().split(', ') if int(number) % 2 == 0] for rows in range(int(input()))]

print(even_matrix)