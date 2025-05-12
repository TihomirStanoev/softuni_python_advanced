from collections import deque




water_quantity = int(input())

queue = deque()

while True:
    command = input()
    if command == 'Start':
        break
    else:
        queue.append(command)


while True:
    command = input()
    if command == 'End':
        break

    elif command.isdigit():
        needed_liters = int(command)
        person = queue.popleft()

        if needed_liters <= water_quantity:
            water_quantity -= needed_liters
            print(f'{person} got water')

        else:
            print(f'{person} must wait')

    elif 'refill' in command:
        _, liters = command.split()
        water_quantity += int(liters)


print(f'{water_quantity} liters left')