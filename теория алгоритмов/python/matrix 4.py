'''
Matrix4. Даны целые положительные числа M, N и набор из N чисел.
Сформировать матрицу размера M × N, у которой в каждой строке содержатся все числа из исходного набора (в том же порядке).
'''
import random
n = int(input())
m = int(input())
mas = []
i = 0
while i < n:
    a = random.randint(-9, 9)
    mas.append(a)
    i += 1
print(mas)
i = 0
matrix = []
while i < m:
    matrix.append(mas)
    i += 1
print(" ") 
i = 0
while i < m:
    print(matrix[i])
    i += 1
