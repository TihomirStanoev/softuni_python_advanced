def move(position, direction, size):
    new_row = DIRECTIONS[direction][0] + position[0]
    new_col = DIRECTIONS[direction][1] + position[1]

    match direction:
        case 'up': new_row = size - 1 if new_row not in range(size) else new_row
        case 'down': new_row = 0 if new_row not in range(size) else new_row
        case 'left': new_col = size - 1 if new_col not in range(size) else new_col
        case 'right': new_col = 0 if new_col not in range(size) else new_col

    return [new_row, new_col]


def create_matrix():
    global bee
    new_matrix = []

    for row in range(n):
        line = list(input())
        processed_line = []
        for char in line:
            if char.isnumeric():
                processed_line.append(int(char))
                continue
            if char == 'B':
                bee = [row, line.index(char)]
            processed_line.append(char)
        new_matrix.append(processed_line)

    return new_matrix


DIRECTIONS = {'down': (1, 0),'up': (-1, 0),'left': (0, -1),'right': (0, 1)}


n = int(input())
bee = [0, 0]
matrix = create_matrix()
energy = 15
needed_nectar = 30
nectar = 0
on_hive = False
bonus_turns = False

while True:
    if energy == 0 and nectar >= needed_nectar and not bonus_turns:
        energy += nectar - needed_nectar
        nectar = needed_nectar
        bonus_turns = True
    elif energy == 0:
        break

    direct = input()
    energy -= 1

    matrix[bee[0]][bee[1]] = '-'
    bee = move(bee, direct, n)
    value = matrix[bee[0]][bee[1]]
    matrix[bee[0]][bee[1]] = 'B'


    if value == 'H':
        on_hive = True
        break
    elif value == '-':
        continue
    else:
        nectar += value


if on_hive:
    if nectar >= 30:
        print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
    else:
        print("Beesy did not manage to collect enough nectar.")
else:
    print("This is the end! Beesy ran out of energy.")

for row in matrix:
    print(*row, sep='')
