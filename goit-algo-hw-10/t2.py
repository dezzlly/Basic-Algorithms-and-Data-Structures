import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Функция для интегрирования
def f(x):
    return x**2

# Пределы интегрирования
a = 0
b = 2

# Метод Монте-Карло
N = 100000
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, b**2, N)  # максимум f(x)=x^2 на [0,2] это 4

under_curve = y_random < f(x_random)
monte_carlo_integral = (b - a) * (b**2) * np.sum(under_curve) / N

# Интеграл через quad
result, error = quad(f, a, b)

# Вывод
print(f"Интеграл методом Монте-Карло: {monte_carlo_integral}")
print(f"Интеграл через quad: {result}, Погрешность: {error}")
