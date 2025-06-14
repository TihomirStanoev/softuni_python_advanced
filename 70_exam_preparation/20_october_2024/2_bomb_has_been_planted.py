def move(old_position, direct):
    new_position = [old_position[0],old_position[1]]
    new_row = old_position[0] + DIRECTIONS[direct][0]
    new_col = old_position[1] + DIRECTIONS[direct][1]

    if new_row in range(n) and new_col in range(m):
        new_position = [new_row, new_col]

    return new_position


DIRECTIONS = {'down': (1, 0),'up': (-1, 0),'left': (0, -1),'right': (0, 1)}
n,m = list(map(int, input().split(', ')))
game_map = []
ct = []
initial_position = []
initial_time = 16
needed_time = 0
on_bomb = False
is_killed = False
bomb_exploded = False

for row in range(n):
    line = list(input())
    if 'C' in line:
        ct = [row, line.index('C')]
        initial_position = [row, line.index('C')]
    game_map.append(line)


game_map[initial_position[0]][initial_position[1]] = '*'

while initial_time > 0:
    command = input()

    if command in DIRECTIONS.keys():
        initial_time -= 1
        on_bomb = False
        next_move = move(ct, command)
        map_value = game_map[next_move[0]][next_move[1]]
        ct = [next_move[0], next_move[1]]


        if map_value == 'B':

            on_bomb = True
            continue

        elif map_value == 'T':
            game_map[next_move[0]][next_move[1]] = '*'
            is_killed = True


        if is_killed:
            break

    else:
        if on_bomb:
            time_left = initial_time - 4

            if time_left >= 0:
                game_map[ct[0]][ct[1]] = 'D'
                break
            else:
                needed_time = abs(time_left)
                game_map[ct[0]][ct[1]] = 'X'
                bomb_exploded = True
                break
        else:
            initial_time -=2


game_map[initial_position[0]][initial_position[1]] = 'C'


if initial_time <= 0 and game_map[ct[0]][ct[1]] != 'D':
    bomb_exploded = True

if bomb_exploded:
    print('Terrorists win!')
    print('Bomb was not defused successfully!')
    print(f'Time needed: {needed_time} second/s.')
elif is_killed:
    print('Terrorists win!')
else:
    print('Counter-terrorist wins!')
    print(f'Bomb has been defused: {initial_time - 4} second/s remaining.')

for r in game_map:
    print(*r, sep='')
