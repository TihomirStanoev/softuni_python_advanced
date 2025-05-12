some_string = list(input())

stack = list()

for index in range(len(some_string)):
    stack.append(some_string.pop())

print(''.join(stack))