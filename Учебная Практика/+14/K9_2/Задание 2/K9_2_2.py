#Выполнил: Зайцев Никита
#Группа: П2-18
'''
К9_2. Техника работы с циклом for и генераторами списков

Задание 2. Array57. Дан целочисленный массив A размера N. Переписать в новый целочисленный массив B
того же размера вначале все элементы исходного массива с четными номерами,
а затем — с нечетными:
A[0], A[2], A[4], A[6], ..., A[1], A[3], A[5], ... .
Условный оператор не использовать.
'''

from random import randint

n = int(input())
a = []
b = []
for i in range(n):
    a.append(randint(1, 100))
print(a)
print(len(a))
for i in range(0, len(a), 2):
    b.append(a[i])
for i in range(1, len(a), 2):
    b.append(a[i])

print(b)
print(len(b))
