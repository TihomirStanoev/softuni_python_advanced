from collections import deque

def fill_the_box(*args):
    height, length, width = args[:3]
    cubes = deque(args[3:])
    cubes_inside, cubes_left = [], []
    current_space = height * length * width


    while True:
        left_cube = cubes.popleft()
        if left_cube == 'Finish':
            break

        current_cube = 0
        while current_space != 0 and left_cube != 0:
            current_cube += 1
            left_cube -= 1
            current_space -= 1

        if current_cube > 0:
            cubes_inside.append(current_cube)
        if left_cube > 0:
            cubes_left.append(left_cube)

    if current_space == 0:
        return f'No more free space! You have {sum(cubes_left)} more cubes.'
    return f'There is free space in the box. You could put {current_space} more cubes.'



print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))