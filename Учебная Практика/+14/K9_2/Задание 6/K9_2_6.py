#Выполнил: Зайцев Никита
#Группа: П2-18
'''
К9_2. Техника работы с циклом for и генераторами списков

Задание 6. Matrix88. Дана квадратная матрица порядка M. Обнулить элементы матрицы,
лежащие ниже главной диагонали. Условный оператор не использовать.
'''

from random import randint


m = int(input())    # Количество строчек
n = int(input())    # Количество столбцов

mtrx =[[randint(1, 10) for j in range(n)] for i in range(m)]    # Заполнение матрицы
print(*['\n'.join((' '.join([str(j) for j in i])) for i in mtrx)])

for i in range(1,m):
    for j in range(i):
        mtrx[i][j] = 0

print()
print(*['\n'.join((' '.join([str(j) for j in i])) for i in mtrx)])
