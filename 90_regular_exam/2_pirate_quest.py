
def index_calc(i,m):
    return i if i in range(m) else i % m

def ship_move(current_pos, direction, n):
    row, col = current_pos[0], current_pos[1]
    match direction:
        case 'up': row -= 1
        case 'down': row += 1
        case 'left': col -= 1
        case 'right': col += 1

    return index_calc(row, n), index_calc(col, n)



def create_map(empty_map, n):
    position = None
    new_map = []
    total_treausers = 0

    for row in range(n):
        line = list(input())
        for col, el in enumerate(line):
            if el == 'S':
                position = [row, col]
                line[col] = '.'
            elif el == '*':
                total_treausers += 1
        new_map.append(line)

    return new_map, position, total_treausers



size = int(input())
MONSTER = 25
MAX_DURABILITY = 100
CHARM = 25
durability = MAX_DURABILITY
is_charm = True
sea_map = []
sea_map, ship, treasures = create_map(sea_map, size)


while durability > 0 and treasures > 0:
    command = input()
    if command == 'stop':
        if treasures > 0:
            print('Retreat! Some treasures remain unclaimed.')
        break

    next_pos = ship_move(ship, command, size)
    element = sea_map[next_pos[0]][next_pos[1]]
    sea_map[ship[0]][ship[1]] = '.'
    sea_map[next_pos[0]][next_pos[1]] = 'S'
    ship = [next_pos[0], next_pos[1]]

    if element == '*':
        treasures -= 1
    elif is_charm and element == 'C':
        durability = min(durability + CHARM, MAX_DURABILITY)
        is_charm = False
    elif element == 'M':
        durability -= MONSTER




if durability <= 0:
    print(f'Shipwreck! Last known coordinates ({ship[0]}, {ship[1]})')
if treasures == 0:
    print('Yo-ho-ho! All treasure chests collected!')


print(f'Ship Durability: {durability}')
if treasures > 0:
    print(f'Unclaimed chests: {treasures}')
[print(*r,sep='') for r in sea_map]