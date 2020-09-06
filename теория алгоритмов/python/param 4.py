'''
Описать процедуру Inv(A, N), меняющую порядок следования элементов вещественного массива A размера N на обратный (инвертирование массива).
Массив A является входным и выходным параметром.
С помощью этой процедуры инвертировать массивы A, B, C размера NA, NB, NC соответственно.
'''
import random
def Inv(A, N):
    i = 0
    while i < N/2:
        A[i], A[N-1-i] = A[N-1-i], A[i]
        i += 1
    print("Inv: ")
    print(A)
n = int(input("N: "))
a = []
b = []
c = []
i = 0
while i < n:
    a.append(random.randint(-9, 9))
    b.append(random.randint(-9, 9))
    c.append(random.randint(-9, 9))
    i += 1
print("A: ")
print(a)
Inv(a, n)
print("B: ")
print(b)
Inv(b, n)
print("C: ")
print(c)
Inv(c, n)
