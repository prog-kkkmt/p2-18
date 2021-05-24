#Выполнили Воронцов Александр, Бурлаев Захар

"""
Данная программа выводит графики в соответсвтвии с координатами X и Y
"""

import matplotlib.pyplot as plt

# Координаты точек по x
x = [1, 5, 10, 15, 20]

# Координаты точек графика first по оси y
y1 = [1, 7, 3, 5, 11]

# Координаты точек графика second по оси y
y2 = [4, 3, 1, 8, 12]

# Координаты точек графика third по оси y
y3 = [5, 6, 4, 7, 13]

plt.figure(figsize=(7, 4)) # Размер рисунка

# Построение графика first
plt.plot(x, y1, 'o-r', alpha=0.7, label="first", lw=5, mec='b', mew=2, ms=10)

# Построение графика second
plt.plot(x, y2, 'v-.g', label="second", mec='r', lw=2, mew=2, ms=12)

# Построение графика third
plt.plot(x, y3, 'o-.m', label="third", mec='r', lw=3, mew=4, ms=13)
plt.legend() # Отображение легенды
plt.grid(True) # Отображение сетки
plt.show() # Отображение графика
