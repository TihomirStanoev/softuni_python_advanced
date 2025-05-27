def recursive_power(x, p):
    if p == 1:
        return x
    return x * recursive_power(x, p-1)


print(recursive_power(2, 10))
print(recursive_power(10, 100))