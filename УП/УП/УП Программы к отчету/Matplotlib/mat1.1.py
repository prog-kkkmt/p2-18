import matplotlib.pyplot as plt
import numpy as np

n = [0, 1, 2, 3, 4]
fig, ax = plt.subplots() # Получение фигуры и оси
ax.plot(n, n, label="График") # Начертить график
ax.set_xlabel("Ось x") # Подписи осей
ax.set_ylabel("Ось y")
ax.set_title("График") # Заголовок фигуры
ax.legend() # Показать легенду
plt.show()
