from collections import deque

contestants = deque(map(int, input().split()))
pies = list(map(int, input().split()))



while contestants and pies:
    pie = pies.pop()
    contestant = contestants.popleft()

    if contestant - pie >= 0:
        contestant -= pie
        if contestant > 0:
            contestants.append(contestant)

    else:
        pie -= contestant

        if pie == 1 and len(pies) >= 1:
            pies[-1] += pie
        elif pie > 0:
            pies.append(pie)




if not pies and not contestants:
    print('We have a champion!')
elif not pies:
    print('We will have to wait for more pies to be baked!')
    print(f"Contestants left: {', '.join(str(c) for c in contestants)}")
elif not contestants:
    print('Our contestants need to rest!')
    print(f"Pies left: {', '.join(str(p) for p in pies)}")

