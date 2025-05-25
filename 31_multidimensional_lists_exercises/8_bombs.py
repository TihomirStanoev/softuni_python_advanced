def coordinates_lst(coordinates_str):
    row_lst = coordinates_str.split()
    coordinates_matrix = []
    for co in row_lst:
        row_m, col_m = list(map(int, co.split(',')))
        coordinates_matrix.append((row_m, col_m))

    return coordinates_matrix

def calculate_alive_and_sum(matrix):
    t_sum,alive  = 0, 0

    for row in matrix:
        for mine in row:
            if mine > 0:
                alive += 1
                t_sum += mine

    return t_sum, alive



n = int(input())
bombs = [[int(x) for x in input().split()] for row in range(n)]
coordinates = coordinates_lst(input())
directions = [(-1,-1),(-1,0),(-1,+1),(0,-1),(0,+1),(+1,-1),(+1,0),(+1,+1)]


for row, col in coordinates:
    bomb = bombs[row][col]
    if bomb > 0:

        for r, c in directions:
            check_r, check_c = row + r, col + c
            if check_r in range(n) and check_c in range(n):
                current_bomb = bombs[check_r][check_c]

                if current_bomb > 0:
                    bombs[check_r][check_c] -= bomb


        bombs[row][col] = 0


total_sum, alive_cells = calculate_alive_and_sum(bombs)

print(f'Alive cells: {alive_cells}')
print(f'Sum: {total_sum}')
[print(*row) for row in bombs]