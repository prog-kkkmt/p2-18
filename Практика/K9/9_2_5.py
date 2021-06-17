#http://ptaskbook.com/ru/tasks/matrix.php
#Matrix56
#Выполнили: Щепкин М.В. П2-18

"""
Дана матрица размера M x N (N — четное число). Поменять местами 
левую и правую половины матрицы.
"""

import random

m = int(input())
n = int(input())

a =  [[random.randint(0, 10)for j in range(n)] for i in range(m)]
temp = []
print(*a, sep = "\n")
for i in range(0, m):
    for j in range(0, n//2):
        a[i][j], a[i][n//2+j] = a[i][n//2+j], a[i][j]
print("\*****************/")
print(*a, sep = "\n")
