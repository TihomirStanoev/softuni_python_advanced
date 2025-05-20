rows = int(input())


matrix = []

for row in range(rows):
    matrix.append(list(input()))
symbol = input()


char_position = None

for row in range(len(matrix)):
    if char_position:
        break
    for col in range(len(matrix[row])):
        if matrix[row][col] == symbol:
            char_position = (row, col)
            break

print(f'{symbol} does not occur in the matrix') if not char_position else print(char_position)