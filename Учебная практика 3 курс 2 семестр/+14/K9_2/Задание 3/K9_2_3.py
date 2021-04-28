#Выполнил: Кузнецов Матвей
#Группа: П2-18
'''
К9_2. Техника работы с циклом for и генераторами списков

Задание 3. Array58. Дан массив A размера N. Сформировать новый массив B того же размера по
следующему правилу: элемент B[K] равен сумме элементов массива A с номерами от 0 до K.
'''

from random import randint

n = int(input())
a = []
b = []
for i in range(n):
    a.append(randint(1, 10))
print(a)
summ = 0
for i in range(len(a)):
    summ += a[i]
    b.append(summ)
print(b)