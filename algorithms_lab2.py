import math
import matplotlib.pyplot as plt

a = 0
b = 1
h = 0.05
y0 = 1

n = int(round((b - a) / h))


def f(x, y):
    return x * math.exp(-x**2) - 2 * x * y


print("Число шагов:", n)


x_euler = [a]
y_euler = [y0]

for i in range(n):
    x_next = x_euler[-1] + h
    y_next = y_euler[-1] + h * f(x_euler[-1], y_euler[-1])

    x_euler.append(x_next)
    y_euler.append(y_next)


x_rk4 = [a]
y_rk4 = [y0]

for i in range(n):
    x_current = x_rk4[-1]
    y_current = y_rk4[-1]

    k1 = h * f(x_current, y_current)
    k2 = h * f(x_current + h / 2, y_current + k1 / 2)
    k3 = h * f(x_current + h / 2, y_current + k2 / 2)
    k4 = h * f(x_current + h, y_current + k3)

    y_next = y_current + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    x_next = x_current + h

    x_rk4.append(x_next)
    y_rk4.append(y_next)


y_exact_1 = 3 / (2 * math.e)

error_euler = abs(y_euler[-1] - y_exact_1)
error_rk4 = abs(y_rk4[-1] - y_exact_1)


print("Метод Эйлера: y(1) =", y_euler[-1])
print("Метод Рунге—Кутты: y(1) =", y_rk4[-1])
print("Точное значение y(1):", y_exact_1)
print("Погрешность метода Эйлера:", error_euler)
print("Погрешность метода Рунге—Кутты:", error_rk4)


print("\nТаблица значений:")
print(f"{'x':>6} {'Точное y':>16} {'Эйлер':>16} {'Рунге—Кутта':>16}")

for i in range(n + 1):
    x = x_euler[i]
    y_exact = (1 + x**2 / 2) * math.exp(-x**2)

    print(
        f"{x:6.2f} "
        f"{y_exact:16.9f} "
        f"{y_euler[i]:16.9f} "
        f"{y_rk4[i]:16.9f}"
    )


x_graph = [a + i * (b - a) / 200 for i in range(201)]
y_graph = [(1 + x**2 / 2) * math.exp(-x**2) for x in x_graph]


plt.figure(figsize=(8, 5))

plt.plot(x_graph, y_graph, label="Точное решение")
plt.plot(x_euler, y_euler, "o--", label="Метод Эйлера")
plt.plot(x_rk4, y_rk4, "o-", label="Метод Рунге—Кутты")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Сравнение решений")
plt.grid(True)
plt.legend()

plt.savefig("grafik.png", dpi=300)
plt.show()