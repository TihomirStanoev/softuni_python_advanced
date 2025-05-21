rows, cols = [int(num) for num in input().split()]

char = ord('a')

for row in range(rows):
    for col in range(cols):
        print(f'{chr(char + row)}{chr(char + col + row)}{chr(char + row)}', end=' ')
    print()