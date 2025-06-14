def next_move(old_pos, direct, size):
    new_row = old_pos[0] + DIRECTIONS[direct][0]
    new_col = old_pos[1] + DIRECTIONS[direct][1]

    if new_col not in range(size) or new_row not in range(size):
        new_row = 0
        new_col = 0

    return [new_row, new_col]


initial_starts = 2
field_size = int(input())
star_field = []
player = []
starts = initial_starts
DIRECTIONS = {'down': (1, 0),'up': (-1, 0),'left': (0, -1),'right': (0, 1)}

for row in range(field_size):
    line = list(input().split())
    if 'P' in line:
        player = [row, line.index('P')]
    star_field.append(line)


while 10 > starts > 0:
    direction = input()

    next_pos = next_move(player, direction, field_size)
    value = star_field[next_pos[0]][next_pos[1]]

    if value == '#':
        starts -= 1
        continue
    elif value == '*':
        starts += 1

    star_field[next_pos[0]][next_pos[1]] = 'P'
    star_field[player[0]][player[1]] = '.'
    player[0], player[1] = next_pos[0], next_pos[1]


if starts == 10:
    print('You won! You have collected 10 stars.')
else:
    print('Game over! You are out of any stars.')
print(f'Your final position is {player}')

for row in star_field:
    print(*row)

