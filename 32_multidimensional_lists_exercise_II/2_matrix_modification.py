def is_valid(r,c,m):
    return r in range(m) and c in range(m)

def add_val(mx, r,c,v):
    mx[r][c] += v
    return mx

def subtract_val(mx, r,c,v):
    mx[r][c] -= v
    return mx


n = int(input())
matrix = [[int(n) for n in input().split()] for _ in range(n)]


while True:
    command = input()
    if command == 'END':
        break
    func, row, col, value = list(map(lambda x: int(x) if x.isnumeric() else str(x), command.split()))

    if not is_valid(row, col, n):
        print('Invalid coordinates')
        continue

    if func == 'Add':
        matrix = add_val(matrix, row, col, value)
    elif func == 'Subtract':
        matrix = subtract_val(matrix, row, col, value)


for row in matrix:
    print(*row)