#Выполнил: Безбородов Константин
#Группа: П2-18
'''
К9_2. Техника работы с циклом for и генераторами списков

Задание 4. Matrix3. Даны целые положительные числа M, N и набор из M чисел. Сформировать
матрицу размера M x N, у которой в каждом столбце содержатся все числа из исходного
набора (в том же порядке).
'''

from random import randint

m = int(input())
n = int(input())

a = [randint(1, 10) for i in range(m)]
print(a)
mtrx1 = []
for i in range(m):
    list_ = []
    for j in range(n):
        list_.append(a[i])
    mtrx1.append(list_)

[print(' '.join([str(j) for j in i])) for i in mtrx1]
