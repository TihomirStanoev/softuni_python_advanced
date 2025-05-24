def valid_index(index, n):
    return 0 <= index < n


def remove_k(current_knights):
    current_left_knight = [None, None, 0]

    for current_knight_row, current_knight_col, current_knight_value in current_knights:
        if current_knight_value > current_left_knight[2]:
            current_left_knight = [current_knight_row, current_knight_col, current_knight_value]

    return current_left_knight[0], current_left_knight[1]


def attack(brd,r,c,i):
    l_pattern = (
        (-2, -1), (-2, +1),
        (+2, -1), (+2, +1),
        (-1, -2), (-1, +2),
        (+1, -2), (+1, +2)
    )
    attacks = 0

    for attack_row, attack_col in l_pattern:
        inner_row, inner_col = attack_row + r, attack_col + c

        if valid_index(inner_row, i) and valid_index(inner_col, i):
            if brd[inner_row][inner_col] == 'K':
                attacks += 1

    return attacks


n = int(input())
board = [list(input()) for _ in range(n)]


knights = []
total_attacks = 0

while True:

    for row in range(n):
        for col in range(n):
            if board[row][col] == 'K':
                knights_attacks = attack(board,row,col,n)
                if knights_attacks > 0:
                    knights.append([row,col,knights_attacks])

    if knights:
        removed_knight_row, removed_knight_col = remove_k(knights)
        board[removed_knight_row][removed_knight_col] = '0'
        total_attacks += 1

    else:
        break


    knights.clear()

print(total_attacks)

