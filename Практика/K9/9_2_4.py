#http://ptaskbook.com/ru/tasks/matrix.php
#Matrix3
#Выполнили: Щепкин М.В. П2-18

"""
Даны целые положительные числа M, N и набор из M чисел.
Сформировать матрицу размера M x N, у которой в каждом столбце
содержатся все числа из исходного набора (в том же порядке).
"""

m = int(input('число строк '))
n = int(input('число столбцов '))
a = [int(input()) for i in range(m)]
b = [[a[j]]*n for j in range(m)]
print(*b, sep='\n')

