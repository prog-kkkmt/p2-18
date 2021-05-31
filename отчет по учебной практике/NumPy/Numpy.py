
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
'''возвращает одномерный массив из указанного количества элементов.'''

def sigmoid(alpha):
    return 1 / ( 1 + np.exp(- alpha * x) )
'''Сигмоидная функция.'''

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
'''Функция указывающая размеры графика.'''

plt.plot(x, sigmoid(0.5), 'ro-')
plt.plot(x, sigmoid(1.0), 'go-')
plt.plot(x, sigmoid(2.0), 'bo-')
'''Переменная указывающася цвет.'''

plt.legend(['A = 0.5', 'A = 1.0', 'A = 2.0'], loc = 'upper left')
'''Легенда в верхнем правом углу.'''

fig.savefig('sigmoid.png')
'''Сохранение PNG-картинки.'''
