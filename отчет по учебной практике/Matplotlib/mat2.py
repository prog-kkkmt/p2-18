import matplotlib.pyplot as plt
import numpy as np
# Установка столбцов по значениям
p = [f"P{i}" for i in range(5)]
# Значения первой группы столбцов
g1 = [10, 21, 34, 12, 27]
# Значения второй группы столбцов
g2 = [17, 15, 25, 21, 26]
width = 0.3 # Ширина столбцов
# [0, 1, 2, 3, 4]
x = np.arange(len(p))
# Размещение графиков рядом друг с другом
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, g1, width, label='g1')
rects2 = ax.bar(x + width/2, g2, width, label='g2')
ax.set_title('Пример групповой диаграммы')
# Список местоположений тиков по оси x
ax.set_xticks(x)
# Возвращает список текстовых экземпляров
ax.set_xticklabels(p)
# Отображение легенды
ax.legend()
plt.show()