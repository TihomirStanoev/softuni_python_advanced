def move(current_pos, direction):
    new_position = [current_pos[0] + DIRECTIONS[direction][0], current_pos[1] + DIRECTIONS[direction][1]]
    if new_position[0] not in range(n) or new_position[1] not in range(n):
        return False
    return new_position

INITIAL_MONEY = 100
money = INITIAL_MONEY
DIRECTIONS = {'down': (1, 0),'up': (-1, 0),'left': (0, -1),'right': (0, 1)}
n = int(input())
position = None
board = []
is_win = True

for r in range(n):
    line = list(input())
    if 'G' in line:
        position = [r, line.index('G')]
        line[line.index('G')] = '-'
    board.append(line)

command = input()

while command != 'end':
    next_move = move(position, command)
    if not next_move:
        is_win = False
        break
    value = board[next_move[0]][next_move[1]]
    board[next_move[0]][next_move[1]] = 'G'
    board[position[0]][position[1]] = '-'
    position = next_move

    if value == 'W':
        money += 100
    elif value == 'P':
        money -= 200
    elif value == 'J':
        money += 100_000
        print('You win the Jackpot!')
        is_win = True
        break

    if money <= 0:
        is_win = False
        break

    command = input()


if is_win:
    print(f'End of the game. Total amount: {money}$')
    [print(*x, sep='') for x in board]
else:
    print('Game over! You lost everything!')