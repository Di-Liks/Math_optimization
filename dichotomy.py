def f(x):
    return 2 * x**2 - 2 * x + 5/2

def dichotomy_method(a, b, epsilon):
    iterations = 0
    while (b - a) >= epsilon:
        iterations += 1
        # Находим середину отрезка
        c = (a + b) / 2
        # Вычисляем две точки с отступом epsilon от середины
        c1 = c - epsilon
        c2 = c + epsilon
        # Сравниваем значения функции в точках c1 и c2
        if f(c1) < f(c2):
            b = c
        else:
            a = c
        print(f"Итерация {iterations}: [a, b] = [{a}, {b}], точка минимума = {(a + b) / 2}")

    # Возвращаем середину полученного отрезка
    return (a + b) / 2

# Задаем начальные значения
a = 1
b = 9
epsilon = 0.2

# Вызываем метод дихотомии
min_x = dichotomy_method(a, b, epsilon)
min_value = f(min_x)

print("\nТочка минимума:", min_x)
print("Значение в точке:", min_value)
