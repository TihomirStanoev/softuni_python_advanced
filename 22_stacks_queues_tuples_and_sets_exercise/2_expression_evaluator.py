from collections import deque
from math import floor

string_input = input().split()
numbers = deque(x for x in string_input)

calcs = deque()
operators = "+*-/"


while numbers:
    char = numbers.popleft()

    if char in operators:
        number = int(calcs.popleft())
        while calcs:
            if char == '+':
                number += int(calcs.popleft())
            elif char == '-':
                number -= int(calcs.popleft())
            elif char == '*':
                number *= int(calcs.popleft())
            elif char == '/':
                number = floor(number / int(calcs.popleft()))
        calcs.append(number)
    else:
        calcs.append(char)


print(calcs[0])