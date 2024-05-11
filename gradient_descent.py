import math

def f(x1, x2):
    return 8*x1**2 + x2**2 - x1*x2 + x1

def grad_f(x1, x2):
    df_dx1 = 16*x1 - x2 + 1
    df_dx2 = 2*x2 - x1
    return df_dx1, df_dx2

def fibonacci_search(f, x1, x2, d, tol=1e-5, max_iter=100):
    a, b = 0, 1
    for _ in range(max_iter):
        if b - a < tol:
            break
        lambda_ = a + (1 - 1e-9) * (b - a)
        mu_ = a + 1e-9 * (b - a)
        if f(x1 + lambda_ * d[0], x2 + lambda_ * d[1]) < f(x1 + mu_ * d[0], x2 + mu_ * d[1]):
            a, b = a, mu_
        else:
            a, b = lambda_, b
    return (a + b) / 2

def gradient_descent_fibonacci(f, grad_f, x1, x2, tol=1e-5, max_iter=100):
    for _ in range(max_iter):
        df_dx1, df_dx2 = grad_f(x1, x2)
        if math.sqrt(df_dx1**2 + df_dx2**2) < tol:
            break
        direction = (-df_dx1, -df_dx2)
        step_size = fibonacci_search(f, x1, x2, direction)
        x1 += step_size * direction[0]
        x2 += step_size * direction[1]
    return x1, x2

# Начальная точка
x1 = 2
x2 = 2

# Минимизация функции
result_x1, result_x2 = gradient_descent_fibonacci(f, grad_f, x1, x2)

print("Минимум функции:", result_x1, result_x2)
print("Значение функции в минимуме:", f(result_x1, result_x2))
