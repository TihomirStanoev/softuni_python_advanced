from functools import reduce

def operate(operator, *args):
    match operator:
        case '+': return reduce(lambda x,y: x+y, args)
        case '-': return reduce(lambda x,y: x-y, args)
        case '*': return reduce(lambda x,y: x*y, args)
        case '/': return reduce(lambda x,y: x/y, args)




print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))