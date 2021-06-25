# Выполнил:Степаненко Кирилл Алексеевич
# Группа: П2-18

# Array58. Дан массив A размера N. Сформировать новый массив B того же размера по
# следующему правилу: элемент B[K] равен сумме элементов массива A с номерами от 0 до K.

from random import random
n = int(input("n = "))
a = []
b = []
for i in range(n):
    c = int(random() * 50)
    a.append(c)
print(a)
s = 0
for i in range(n-1,-1,-1):
     s = s+a[i]
     b.insert(0,s)
print(b)
