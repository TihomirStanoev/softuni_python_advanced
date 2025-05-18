from collections import deque

def convert_time(time):
    the_time = ''
    if isinstance(time, str):
        h, m, s = list(map(int, time.split(':')))
        the_time = (h * 60 * 60) + (m * 60) + s

    elif isinstance(time, int):
        h = time // 3600
        m = (time - (h * 3600)) // 60
        s = time - (h * 3600) - (m * 60)
        the_time = f'{h%24:02d}:{m:02d}:{s:02d}'

    return the_time



all_robots = input().split(';')
start_time = input()

robots = []

for robot in all_robots:
    name, process_time = robot.split('-')
    new_robot = {'name': name, 'process time': int(process_time), 'end time': 0}
    robots.append(new_robot)

start_time = convert_time(start_time)


waited_parts = deque()

while True:
    command = input()
    if command == 'End':
        break
    waited_parts.append(command)



while waited_parts:
    start_time += 1
    current_part = waited_parts.popleft()

    for robot in robots:
        if robot['end time'] <= start_time:
            robot['end time'] = robot['process time'] + start_time
            print(f"{robot['name']} - {current_part} [{convert_time(start_time)}]")
            break
    else:
        waited_parts.append(current_part)
