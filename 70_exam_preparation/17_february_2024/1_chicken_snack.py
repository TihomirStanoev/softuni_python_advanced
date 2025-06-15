from collections import deque

pocket_money = list(map(int, input().split()))
foods_prices = deque(map(int, input().split()))
foods = 0

while pocket_money and foods_prices:
    money = pocket_money.pop()
    price = foods_prices.popleft()

    if money == price:
        foods += 1
    elif money > price:
        foods += 1
        if pocket_money:
            pocket_money[-1] += money - price


if foods >= 4:
    print(f'Gluttony of the day! Henry ate {foods} foods.')
elif foods > 1:
    print(f'Henry ate: {foods} foods.')
elif foods > 0:
    print(f'Henry ate: {foods} food.')
else:
    print('Henry remained hungry. He will try next weekend again.')