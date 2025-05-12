expression = list(input())

parentheses_stack = list()

for index in range(len(expression)):
    if expression[index] == '(':
        parentheses_stack.append(index)
    elif expression[index] == ')':
        start_index = parentheses_stack.pop()
        last_index = index
        print(''.join(expression[start_index:last_index + 1]))


