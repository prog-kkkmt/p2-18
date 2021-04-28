#Выполнил: Кузнецов Матвей
#Группа: П2-18
'''
import matplotlib.pyplot as plt
# Координаты точек по x
x = [1, 5, 10, 15, 20]
# Координаты точек графика first по оси y
y1 = [1, 7, 3, 5, 11]
# Координаты точек графика second по оси y
y2 = [4, 3, 1, 8, 12]
plt.figure(figsize=(7, 4)) # Размер рисунка
# Построение графика first
plt.plot(x, y1, 'o-r', alpha=0.7, label="first", lw=5, mec='b', mew=2, ms=10)
# Построение графика second
plt.plot(x, y2, 'v-.g', label="second", mec='r', lw=2, mew=2, ms=12)
plt.legend() # Отображение легенды
plt.grid(True) # Отображение сетки
plt.show() # Отображение графика