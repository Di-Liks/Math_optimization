import math
# Определим функцию и её градиент
def f(x):
    x1, x2 = x
    return 8 * x1 ** 2 + x2 ** 2 - x1 * x2 + x1
def grad_f(x):
    x1, x2 = x
    df_dx1 = 16 * x1 - x2 + 1
    df_dx2 = 2 * x2 - x1
    return [df_dx1, df_dx2]
# Метод одномерного поиска для определения оптимального шага alpha
def minimize_alpha(f, x_k, d_k, grad_k, alpha_init=1.0, rho=0.5, c=1e-4):
    alpha = alpha_init
    while f([x_k[i] + alpha * d_k[i] for i in range(len(x_k))]) > f(x_k) + c * alpha * sum(
            [grad_k[i] * d_k[i] for i in range(len(grad_k))]):
        alpha *= rho
    return alpha
# Метод Флетчера-Ривса
def fletcher_reeves(f, grad_f, x0, epsilon, max_iter):
    x_k = x0[:]
    grad_k = grad_f(x_k)
    d_k = [-g for g in grad_k]
    k = 0
    while math.sqrt(sum(g ** 2 for g in grad_k)) > epsilon and k < max_iter:
        # Поиск шага alpha_k
        alpha_k = minimize_alpha(f, x_k, d_k, grad_k)
        # Обновление x_k
        x_k = [x_k[i] + alpha_k * d_k[i] for i in range(len(x_k))]
        # Обновление градиента
        grad_k_new = grad_f(x_k)
        # Вычисление беты
        beta_k = sum(g ** 2 for g in grad_k_new) / sum(g ** 2 for g in grad_k)
        # Обновление направления
        d_k = [-grad_k_new[i] + beta_k * d_k[i] for i in range(len(grad_k))]
        # Вывод промежуточных результатов
        print(
            f"Итерация {k}: x = {x_k}, f(x) = {f(x_k)}, ||grad_f(x)|| = {math.sqrt(sum(g ** 2 for g in grad_k))}, alpha = {alpha_k}")
        # Подготовка к следующей итерации
        grad_k = grad_k_new[:]
        k += 1
    return x_k, f(x_k)
# Параметры алгоритма
epsilon = 0.1
x0 = [2, 2]
max_iter = 1000
# Запуск алгоритма
x_min, f_min = fletcher_reeves(f, grad_f, x0, epsilon, max_iter)
print(f"\nМинимум функции достигается в точке: {x_min}")
print(f"Значение функции в этой точке: {f_min}")
