the_string = list(input().split())
the_stack = list()

for _ in range(len(the_string)):
    the_stack.append(the_string.pop())

print(' '.join(the_stack))

