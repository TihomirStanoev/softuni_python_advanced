
INITIAL_ARMOR = 300
TAKEN_DAMAGE = 100
DIRECTIONS = {'down': (1, 0),'up': (-1, 0),'left': (0, -1),'right': (0, 1)}
armor = INITIAL_ARMOR
n = int(input())

airspace = []
jet = None
total_enemies = 0

for r in range(n):
    line = list(input())
    airspace.append(line)
    if 'J' in line:
        jet = [r, line.index('J')]
        line[line.index('J')] = '-'
    if 'E' in line:
        total_enemies += line.count('E')



while total_enemies > 0 and armor > 0:
    command = input()
    next_move = [jet[0] + DIRECTIONS[command][0], jet[1] + DIRECTIONS[command][1]]

    value = airspace[next_move[0]][next_move[1]]

    if value == 'R':
        armor = INITIAL_ARMOR
    elif value == 'E':
        armor -= TAKEN_DAMAGE
        if armor > 0 and total_enemies == 1:
            total_enemies -= 1
            print('Mission accomplished, you neutralized the aerial threat!')
        elif armor > 0:
            total_enemies -= 1
        else:
            print(f'Mission failed, your jetfighter was shot down! Last coordinates [{next_move[0]}, {next_move[1]}]!')


    jet = [next_move[0], next_move[1]]
    airspace[jet[0]][jet[1]] = '-'
else:
    airspace[jet[0]][jet[1]] = 'J'

[print(*r, sep='') for r in airspace]
