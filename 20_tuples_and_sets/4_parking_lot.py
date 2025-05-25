cars = set()

for _ in range(int(input())):
    command, number = input().split(', ')
    if command == 'IN':
        cars.add(number)
    elif command == 'OUT':
        if number in cars:
            cars.remove(number)


print(*cars, sep='\n') if cars else print('Parking Lot is Empty')