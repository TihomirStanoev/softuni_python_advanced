from collections import deque

bee_groups = deque(map(int, input().split()))
eaters_groups = list(map(int, input().split()))
kill = 7



while bee_groups and eaters_groups:
    bee = bee_groups[0]
    eater = eaters_groups[-1]

    while True:
        if eater == 0 and bee == 0:
            bee_groups.popleft()
            eaters_groups.pop()
            break
        if eater == 0:
            eaters_groups.pop()
            bee_groups[0] = bee
            bee_groups.append(bee_groups.popleft())
            break
        if bee - kill < 0:
            bee_groups.popleft()
            eaters_groups[-1] = eater
            break
        eater -= 1
        bee -= kill



print('The final battle is over!')

if not bee_groups and not eaters_groups:
    print('But no one made it out alive!')
elif bee_groups:
    print(f"Bee groups left: {', '.join(str(bee) for bee in bee_groups)}")
elif eaters_groups:
    print(f"Bee-eater groups left: {', '.join(str(eater) for eater in eaters_groups)}")