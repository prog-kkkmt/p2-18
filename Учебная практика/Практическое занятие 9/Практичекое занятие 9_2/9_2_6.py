#http://ptaskbook.com/ru/tasks/matrix.php
#Matrix88
#Выполнили: Воронцов А.А. Бурлаев З.С. Щепкин М.В. П2-18

"""
Дана квадратная матрица порядка M. Обнулить элементы матрицы, 
лежащие ниже главной диагонали. Условный оператор не использовать.
"""

import random

m = int(input())
a = [[random.randint(0, 9)for j in range(m)] for i in range(m)]

print(*a, sep = "\n")
for i in range(0, m):
    for j in range(i+1, m):
        a[j][i] = 0
        
print("\****************/")        
print(*a, sep = "\n")
