from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
intelligence = int(input())


barrel_track = 0
while bullets and locks:

    current_lock = locks[0]
    current_bullet = bullets.pop()
    intelligence -= bullet_price

    if current_lock >= current_bullet:
        locks.popleft()
        print('Bang!')
    else:
        print('Ping!')

    barrel_track += 1
    if barrel_track == barrel_size and bullets:
        print('Reloading!')
        barrel_track = 0


if not locks:
    print(f'{len(bullets)} bullets left. Earned ${intelligence}')
elif locks:
    print(f'Couldn\'t get through. Locks left: {len(locks)}')






