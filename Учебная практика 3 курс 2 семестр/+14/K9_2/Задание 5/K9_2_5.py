#Выполнил: Кузнецов Матвей
#Группа: П2-18
'''
К9_2. Техника работы с циклом for и генераторами списков

Задание 5. Matrix56. Дана матрица размера M x N (N — четное число). Поменять местами
левую и правую половины матрицы.
'''

from random import randint
def swap(a, b):
    a, b = b, a

m = int(input())    # Количество строчек
n = int(input())    # Количество столбцов

mtrx =[[randint(1, 10) for j in range(n)] for i in range(m)]    # Заполнение матрицы
print(*['\n'.join((' '.join([str(j) for j in i])) for i in mtrx)])
n1 = n//2

[[swap(mtrx[j], mtrx[j - n1]) for j in range(n1)] for i in range(m)]
print()
print(*['\n'.join((' '.join([str(j) for j in i])) for i in mtrx)])


'''

2 1 10 2 4 3        2 4 3 2 1 10
4 6 4 8 1 10        8 1 10 4 6 4
1 9 3 10 2 6  <=>   10 2 6 1 9 3
10 5 2 4 5 9        4 5 9 10 5 2
9 2 5 10 1 7        7 1 10 9 2 5




'''