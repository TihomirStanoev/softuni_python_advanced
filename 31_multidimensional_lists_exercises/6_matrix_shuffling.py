def is_valid(x1,y1,x2,y2):
    return x1 in range(rows) and y1 in range(cols) and x2 in range(rows) and y2 in range(cols)



rows, cols = [int(num) for num in input().split()]
matrix = [[char for char in input().split()]for row in range(rows)]


while True:
    commands = input()
    if commands == 'END':
        break
    command = commands.split()

    if command[0] != 'swap' or len(command) != 5:
        print('Invalid input!')
        continue

    x_1, y_1, x_2, y_2 = [int(i) for i in command[1:]]
    if is_valid(x_1, y_1, x_2, y_2):
        matrix[x_1][y_1], matrix[x_2][y_2] = matrix[x_2][y_2], matrix[x_1][y_1]
        for row in matrix:
            print(*row)


    else:
        print('Invalid input!')
