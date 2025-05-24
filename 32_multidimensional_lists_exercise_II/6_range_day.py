def print_board():
    [print(*c, sep=' ') for c in shotgun_board]

def on_board(x, y):
    return x in range(N) and y in range(N)

N = 5
shotgun_board = []
current_position = [0,0]
remaining_targets = 0
hit_targets = []
moves = {'up': (-1,0),'down': (1,0),'left': (0,-1),'right': (0,1)}


for row in range(N):
    cols = list(input().split())
    for el in cols:
        if el == 'A':
            col = cols.index(el)
            current_position = [row,col]

            cols[col] = '.'

        elif el == 'x':
            remaining_targets += 1
    shotgun_board.append(cols)


for _ in range(int(input())):
    commands = input().split()
    command, direction = commands[:2]

    if command == 'shoot':
        shot_row = current_position[0] + moves[direction][0]
        shot_col = current_position[1] + moves[direction][1]

        while on_board(shot_row,shot_col):
            if shotgun_board[shot_row][shot_col] == 'x':
                hit_targets.append((shot_row, shot_col))
                shotgun_board[shot_row][shot_col] = '.'
                remaining_targets -= 1
                break
            shot_row += moves[direction][0]
            shot_col += moves[direction][1]

        if remaining_targets == 0:
            break

    elif command == 'move':
        pos_row = current_position[0] + moves[direction][0] * int(commands[2])
        pos_col = current_position[1] + moves[direction][1] * int(commands[2])

        if on_board(pos_row, pos_col) and shotgun_board[pos_row][pos_col] == '.':
            shotgun_board[current_position[0]][current_position[1]] = '.'
            shotgun_board[pos_row][pos_col] = 'A'
            current_position = [pos_row, pos_col]


if remaining_targets == 0:
    print(f'Training completed! All {len(hit_targets)} targets hit.')
else:
    print(f'Training not completed! {remaining_targets} targets left.')


[print(list(target)) for target in hit_targets]