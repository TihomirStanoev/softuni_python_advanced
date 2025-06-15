def move(player, direction, limit):
    new_position = player

    if new_position[0]+DIRECTIONS[direction][0] in range(limit) and new_position[1]+DIRECTIONS[direction][1] in range(limit):
        new_position = [new_position[0]+DIRECTIONS[direction][0], new_position[1]+DIRECTIONS[direction][1]]

    return new_position


MAX_HEALTH = 100
HEALTH_BOOST = 15
health = MAX_HEALTH
damage = 40
DIRECTIONS = {'down': (1, 0),'up': (-1, 0),'left': (0, -1),'right': (0, 1)}
size = int(input())
position = None
maze = []
is_death = False


for row in range(size):
    line = list(input())
    maze.append(line)
    if 'P' in line:
        position = [row, line.index('P')]



while True:
    command = input()
    new_pos = move(position, command, size)
    maze[position[0]][position[1]] = '-'

    value = maze[new_pos[0]][new_pos[1]]

    if value == 'M':
        health -= damage
        if health < 0:
            position = [new_pos[0], new_pos[1]]
            is_death = True
            break

    elif value == 'H':
        health += min(HEALTH_BOOST, MAX_HEALTH-health)

    elif value == 'X':
        position = [new_pos[0], new_pos[1]]
        break

    position = [new_pos[0], new_pos[1]]

maze[position[0]][position[1]] = 'P'


if is_death:
    print('Player is dead. Maze over!')
else:
    print('Player escaped the maze. Danger passed!')

print(f'Player\'s health: {0 if health <= 0 else health} units')
[print(*r, sep='') for r in maze]
