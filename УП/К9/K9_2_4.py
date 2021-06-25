# Выполнил:Степаненко Кирилл Алексеевич
# Группа: П2-18

# Matrix3. Даны целые положительные числа M, N и набор из M чисел.
# Сформировать матрицу размера M x N, у которой в каждом столбце содержатся все числа из исходного
# набора (в том же порядке).

from random import randint

M = int(input())
N = int(input())

mass_a = []
mass_b = [[]]
for i in range(M):
    mass_a.append(randint(1, 100))
print(mass_a)
for i in range(M):
    # for j in range(N):
    mass_b[i][0] = mass_a[i]
print(mass_b)