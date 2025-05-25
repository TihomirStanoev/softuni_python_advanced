presents = int(input())
n = int(input())

moves = {'up': (-1,0),'down': (1,0),'left': (0,-1),'right': (0,1)}
neighborhood = []
santa = []
nice_kids = 0


for row in range(n):
    line = input().split()
    for col, el in enumerate(line):
        if el == 'S':
            santa = [row, col]
        elif el == 'V':
            nice_kids += 1
    neighborhood.append(line)


total_nice_kids = nice_kids

while presents > 0:
    command = input()
    if command == 'Christmas morning':
        break

    ch_row = santa[0] + moves[command][0]
    ch_col = santa[1] + moves[command][1]

    if ch_row not in range(n) and ch_col not in range(n):
        continue

    house = neighborhood[ch_row][ch_col]
    if house == 'V':
        presents -= 1
        nice_kids -= 1


    elif house == 'C':
        for move in moves.values():

            ar_row = ch_row + move[0]
            ar_col = ch_col + move[1]
            around_house = neighborhood[ar_row][ar_col]

            if around_house in ['V','X']:
                presents -= 1
                neighborhood[ar_row][ar_col] = '-'
                nice_kids -= 1 if around_house == 'V' else 0

            if presents == 0:
                break

    neighborhood[santa[0]][santa[1]] = '-'
    santa = [ch_row, ch_col]
    neighborhood[santa[0]][santa[1]] = 'S'


if presents < 1 and nice_kids > 0:
    print(f'Santa ran out of presents!')

[print(*row) for row in neighborhood]


if nice_kids == 0:
    print(f'Good job, Santa! {total_nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids} nice kid/s.')
