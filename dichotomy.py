def f(x):
    return 2*x**2 - 2*x + 5/2
def dichotomy_method(a, b, epsilon):
    iterations = 0
    while (b - a) / 2 > epsilon:
        midpoint = (a + b) / 2
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        iterations += 1
        print(f"Итерация {iterations}: a = {a}, b = {b}, ср. значение = {midpoint}")
    return (a + b) / 2

a = 1
b = 9
epsilon = 0.2

root = dichotomy_method(a, b, epsilon)
print("Точка:", root)
print("Значение функции в точке:", f(root))
