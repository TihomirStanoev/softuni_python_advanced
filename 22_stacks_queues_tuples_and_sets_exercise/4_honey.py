from collections import deque


def calculate_honey(bee, honey, operator):
    bee, honey = abs(bee), abs(honey)
    match operator:
        case '+': return bee + honey
        case '*': return bee * honey
        case '/': return 0 if honey == 0 else bee / honey
        case '-': return abs(bee - honey)
    return 0


working_bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = deque(map(str, input().split()))
total_honey = 0


while working_bees and nectar:
    if working_bees[0] <= nectar[-1]:
        first_bee = working_bees.popleft()
        last_honey = nectar.pop()
        symbol = symbols.popleft()

        total_honey += calculate_honey(first_bee, last_honey, symbol)
    else:
        nectar.pop()
        continue


print(f'Total honey made: {total_honey}')
print('', end='' if not working_bees else f'Bees left: {", ".join(str(bee) for bee in working_bees)}')
print('', end='' if not nectar else f'Nectar left: {", ".join(str(honey) for honey in nectar)}')