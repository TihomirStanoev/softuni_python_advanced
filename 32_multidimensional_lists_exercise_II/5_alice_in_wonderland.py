def next_way(current_position, directions, course):
    next_pos = [current_position[0], current_position[1]]

    next_pos[0] += directions[course][0]
    next_pos[1] += directions[course][1]

    return next_pos



def is_valid(pos, size):
    return pos[0] in range(size) and pos[1] in range(size)


n = int(input())
square = []
alice = []
rabit_hole = ()
moves = {
    'up': (-1,0),
    'down': (1,0),
    'left': (0,-1),
    'right': (0,1),
}

for row in range(n):
    cols = list(input().split())
    if 'A' in cols:
        col = cols.index('A')
        alice = [row,col]
        cols[col] = '*'
    if 'R' in cols:
        col = cols.index('R')
        rabit_hole = (row, col)
    square.append(cols)


total_tea = 0
while total_tea < 10:
    direction = input()
    next_move = next_way(alice, moves, direction)
    next_row, next_col = next_move

    if not is_valid(next_move, n):
        break

    alice = [next_row, next_col]
    square[next_row][next_col] = '*'

    if square[next_row][next_col] in '*.':
        continue

    elif square[next_row][next_col] == 'R':
        break

    elif square[next_row][next_col].isdigit():
        total_tea += int(square[next_row][next_col])



if total_tea >= 10:
    print('She did it! She went to the party.')
else:
    print('Alice didn\'t make it to the tea party.')

[print(*row, sep=' ') for row in square]