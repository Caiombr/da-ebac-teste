def fibonacci(n):
    i = 0
    y = 1
    x = 0

    for num in range(n):
        x = i + y
        i = y
        y = x 
    return print(x)


def perimetro(n):
    perimetro = 4

    i = 0
    y = 1

    for num in range(n):
        x = i + y
        i = y
        y = x 
        perimetro = perimetro + x * 4
        print(x)
    return perimetro