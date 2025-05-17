from collections import deque

def balance_check(parenthesis_str):
    match parenthesis_str:
        case '()' | '[]' | '{}': return True
        case _ : return False


parenthesis = deque(input())
total_parenthesis = len(parenthesis)

is_balance = True
parenthesis_stack = []

while parenthesis and is_balance:
    current_parenthesis = parenthesis.popleft()

    if current_parenthesis in '([{':
        parenthesis_stack.append(current_parenthesis)

    elif current_parenthesis in ')]}':
        if parenthesis_stack:
            last_parenthesis = parenthesis_stack.pop()
            is_balance = balance_check(last_parenthesis + current_parenthesis)
        else:
            is_balance = False
            break


print('YES') if is_balance else print('NO')
