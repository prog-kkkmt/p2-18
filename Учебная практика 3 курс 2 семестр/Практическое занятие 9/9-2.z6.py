# Выполнил Кузнецов М. С. П2-18.
# Дана квадратная матрица порядка M. Обнулить элементы матрицы,
# лежащие ниже главной диагонали. Условный оператор не использовать.

import random as rnd

m = rnd.randrange(2, 10, 2)
n = m
a = [rnd.randrange(0, 100) for i in range(m)]
print('Матрица размером:', m, 'на', m)
b = [a] * n
print(*b, sep='\n')
