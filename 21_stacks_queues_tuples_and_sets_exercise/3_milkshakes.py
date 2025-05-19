from collections import deque

chocolates = list(map(int, input().split(', ')))
milks = deque(map(int, input().split(', ')))


total_chocolates = 0
while chocolates and milks and total_chocolates < 5:
    chocolate = chocolates.pop()
    milk = milks.popleft()

    if chocolate <=0 and milk <=0:
        continue
    elif chocolate <= 0:
        milks.appendleft(milk)
        continue
    elif milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk:
        total_chocolates += 1
    else:
        milks.append(milk)
        chocolate -= 5
        chocolates.append(chocolate)


print('Great! You made all the chocolate milkshakes needed!') if total_chocolates == 5 else print("Not enough milkshakes.")
print("Chocolate: empty") if not chocolates else print(f'Chocolate: {", ".join(str(choko) for choko in chocolates)}')
print("Milk: empty") if not milks else print(f'Milk: {", ".join(str(milk) for milk in milks)}')
