import math

def f(x):
    return 2 * x**2 - 2 * x + 5/2

def golden_section_search(a, b, epsilon):
    gr = (math.sqrt(5) + 1) / 2  # Золотое сечение
    x1 = b - (b - a) / gr
    x2 = a + (b - a) / gr
    iterations = 0

    while abs(b - a) > epsilon:
        iterations += 1
        if f(x1) < f(x2):
            b = x2
        else:
            a = x1

        x1 = b - (b - a) / gr
        x2 = a + (b - a) / gr

        print(f"Итерация {iterations}: [a, b] = [{a:.4f}, {b:.4f}], x1 = {x1:.4f}, x2 = {x2:.4f}")

    return (a + b) / 2

a = 1
b = 9
epsilon = 0.2

minimum = golden_section_search(a, b, epsilon)
print(f"\nМинимум функции на отрезке [1, 9] с точностью 0.2: {minimum:.4f}")
print(f"Значение функции в найденной точке: {f(minimum):.4f}")
