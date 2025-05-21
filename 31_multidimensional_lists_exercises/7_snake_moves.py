from collections import deque

rows, cols = [int(n) for n in input().split()]

matrix = [['' for c in range(cols)] for row in range(rows)]
snake = deque(list(input()))


left_to_right = range(cols)
right_to_left = range(cols - 1, -1, -1)

for row in range(rows):
    _cols = left_to_right if row % 2 == 0 else right_to_left
    for col in _cols:
        matrix[row][col] = snake[0]
        snake.rotate(-1)


for row in matrix:
    print(''.join(row))

