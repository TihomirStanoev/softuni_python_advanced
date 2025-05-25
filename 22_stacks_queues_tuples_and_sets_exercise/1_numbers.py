first = set(map(int, input().split()))
second = set(map(int, input().split()))

n = int(input())


for _ in range(n):
    commands = input().split()
    command, nums = ' '.join(commands[:2]), set(map(int,commands[2:]))


    if command == 'Add First':
        first = first.union(nums)

    elif command == 'Add Second':
        second = second.union(nums)

    elif command == 'Remove First':
        first = first.difference(nums)

    elif command == 'Remove Second':
        second = second.difference(nums)

    elif command == 'Check Subset':
        if first.issubset(second) or second.issubset(first):
            print('True')
        else:
            print('False')

print(', '.join(str(n) for n in sorted(first)))
print(', '.join(str(m) for m in sorted(second)))