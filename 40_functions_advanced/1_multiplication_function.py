def multiply(*arg):
    m = 1
    for n in arg:
        m *= n
    return m



print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))