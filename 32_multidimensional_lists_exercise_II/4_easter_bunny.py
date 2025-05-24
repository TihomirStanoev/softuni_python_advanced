def create_point_list(bunny_dict, board, bunny_position, size):
    bunny_row, bunny_col = bunny_position
    ranges = {
        'up': range(bunny_row - 1, -1, -1),
        'down': range(bunny_row + 1, size),
        'left': range(bunny_col - 1, -1, -1),
        'right': range(bunny_col + 1, size)
    }


    for direction in bunny_dict.keys():
        direction_list = []
        total_points = 0

        for pos in ranges[direction]:
            value,r_row,column  = 0, 0, 0

            if direction == 'up' or direction == 'down':
                r_row, column = pos, bunny_col
            elif direction == 'left' or direction == 'right':
                r_row, column = bunny_row, pos

            value = board[r_row][column]

            if value == 'X':
                break

            direction_list.append([r_row,column])
            total_points += value

        bunny_dict[direction]['points'] = direction_list
        bunny_dict[direction]['total'] = total_points if direction_list else -float('inf')

    return bunny_dict


def higher_direction(direction_dict):
    highest_points = -float('inf')
    direct = None

    for direction in direction_dict.keys():
        if direction_dict[direction]['total'] > highest_points:
            highest_points = direction_dict[direction]['total']
            direct = direction

    return direct



n = int(input())
highest = ''
matrix = []
bunny = ()
directions = {
    'up': {'points': [], 'total': 0},
    'down': {'points': [], 'total': 0},
    'left': {'points': [], 'total': 0},
    'right': {'points': [], 'total': 0},
}



for row in range(n):
    col = list(map(lambda x: int(x) if not x.isalpha() else str(x), input().split()))
    if 'B' in col:
        bunny = (row, col.index('B'))
    matrix.append(col)

directions = create_point_list(directions, matrix, bunny, n)
highest = higher_direction(directions)

print(highest)
print(*directions[highest]['points'], sep='\n')
print(directions[highest]['total'])