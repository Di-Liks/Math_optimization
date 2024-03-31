import math


def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


def f(x):
    return 2 * x ** 2 - 2 * x + 5 / 2


def golden_section_search(f, a, b, epsilon):
    phi = (1 + math.sqrt(5)) / 2
    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi
    f1 = f(x1)
    f2 = f(x2)
    iterations = 0

    while abs(b - a) > epsilon:
        iterations += 1
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = b - (b - a) / phi
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (b - a) / phi
            f2 = f(x2)

        print("Итерация {}: a = {:.5f}, b = {:.5f}, L = {:.5f}".format(iterations, a, b, abs(b - a)))

    return (a + b) / 2, iterations


a = 1
b = 9
epsilon = 0.2
n = 8  # количество итераций для метода Фибоначчи

fib_sequence = fibonacci(n)
L = b - a
for i in range(2, n + 1):
    if fib_sequence[i] > L / epsilon:
        n = i - 2
        break

min_x, iterations = golden_section_search(f, a, b, epsilon)
min_f = f(min_x)

print(f"Минимум функции f(x) = 2x^2 - 2x + 5/2 достигается в точке x = {min_x:.4f}")
print(f"Значение функции в минимуме f(x) = {min_f:.4f}")
print("Количество итераций:", iterations)
