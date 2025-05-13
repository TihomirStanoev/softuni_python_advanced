from collections import deque

def biggest_order(order_deque):
    biggest_ord = 0

    for _ in range(len(order_deque)):
        current_order = order_deque[0]
        if biggest_ord <= current_order:
            biggest_ord = current_order
        order_deque.rotate(1)

    return biggest_ord


quantity_food = int(input())
quantity_order = deque(map(int, input().split()))

highest_order = biggest_order(quantity_order)

for _ in range(len(quantity_order)):
    if quantity_food - quantity_order[0] >= 0:
        quantity_food -= quantity_order[0]
        quantity_order.popleft()
    else:
        break


print(highest_order)

if not quantity_order:
    print('Orders complete')
else:
    print(f'Orders left: ', end='')
    print(' '.join(str(order) for order in quantity_order))