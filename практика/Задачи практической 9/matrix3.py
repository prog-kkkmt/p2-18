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
matrix = []
for i in range(a):
    matrix.append([d[i] for j in range(b)])
print(matrix)
