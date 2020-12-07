#http://ptaskbook.com/ru/tasks/array.php
#Array 58
#Выполнили: Воронцов А.А. Бурлаев З.С. Щепкин М.В. П2-18

"""
Дан массив A размера N.
Сформировать новый массив B того же размера по 
следующему правилу: элемент B[K] равен сумме элементов
массива A с номерами от 0 до K.
"""
n = int(input())
a = [int(input()) for i in range(n)]
b = []
for i in range(n):
    num = sum(range(a[0], a[i]+1))
    b.append(num)
print(b)
