# Выполнил:Степаненко Кирилл Алексеевич
# Группа: П2-18

# Matrix3. Даны целые положительные числа M, N и набор из M чисел.
# Сформировать матрицу размера M x N, у которой в каждом столбце содержатся все числа из исходного
# набора (в том же порядке).

import random
import numpy
a = random.randrange(2,10)
b = random.randrange(2,10)
print("a: ", a, "b: ", b)
c = numpy.zeros((a, b))
d = [random.randrange(1,5) for i in range(a)]
print(a)
print(d)
for i in range(a):
    for j in range(b):
        c[i][j] = d[i]
print(c)
n = []
for i in range(a):
    n.append([d[i] for j in range(b)])
print(n)