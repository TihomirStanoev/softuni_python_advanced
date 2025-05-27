def rectangle(length,width):
    def area(a,b):
        return a * b

    def perimeter(a,b):
        return a * 2 + b * 2

    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    return f'Rectangle area: {area(length, width)}\nRectangle perimeter: {perimeter(length, width)}'



print(rectangle(2, 10))
print(rectangle('2', 10))