n = int(input())

stack = []

for _ in range(n):
    command, *number = input().split()

    match command:
        case '1': stack.append(int(number[0]))
        case '2': stack.pop() if stack else None
        case '3': print(max(stack)) if stack else None
        case '4': print(min(stack)) if stack else None


length_stack = len(stack)

for i in range(length_stack):
    if i != length_stack - 1:
        x = ', '
    else:
        x = ''
    print(stack.pop(), end=x)