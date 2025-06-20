def create_space(size):
    matrix = []
    for row in range(size):
        line = list(input().split())
        matrix.append(line)
    return matrix

def position_locate(size, space):
    position = []
    for row in range(size):
        for col in range(size):
            if space[row][col] == 'S':
                position = [row,col]
                space[row][col] = '.'
    return position, space

def out_space(coordinates,m):
    return True if coordinates[0] in range(m) and coordinates[1] in range(m) else False

def move(direction, position, size):
    new_position = [position[0], position[1]]
    match direction:
        case 'up': new_position[0] -= 1
        case 'down': new_position[0] += 1
        case 'left': new_position[1] -= 1
        case 'right': new_position[1] += 1

    return new_position if out_space(new_position, size) else None



meteorite_decreased = 5
refuel = 10
initially_resources = 100
n = int(input())
space_field = create_space(n)
space_position, space_field = position_locate(n,space_field)
planet_b = False
in_space = True



while not planet_b:

    command = input()
    next_move = move(command, space_position, n)
    if not next_move:
        in_space = False
        break

    initially_resources -= meteorite_decreased
    space_position = next_move
    value = space_field[next_move[0]][next_move[1]]
    space_field[space_position[0]][space_position[1]] = '.' if value != 'R' else 'R'

    if value == 'M':
        initially_resources -= meteorite_decreased
    elif value == 'R':
        initially_resources += min(refuel, 100 - initially_resources)
    elif value == 'P':
        planet_b = True

    if initially_resources <= 0:
        break


if planet_b:
    space_field[space_position[0]][space_position[1]] = 'P'
    print(f'Mission accomplished! The spaceship reached Planet B with {initially_resources} resources left.')
else:
    space_field[space_position[0]][space_position[1]] = 'S'
    if space_position and in_space:
        print('Mission failed! The spaceship was stranded in space.')
    else:
        print('Mission failed! The spaceship was lost in space.')

[print(*x) for x in space_field]
