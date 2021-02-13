"""
https://stepik.org/lesson/543/step/10?unit=866
"""

"""
Реализуйте функцию swap_min, которая принимает на вход двумерный массив целых чисел,
ищет в этом массиве строку, содержащую наименьшее среди всех элементов массива значение, и меняет эту строку местами с первой строкой массива.

Подумайте, как обменять строки массива, не обменивая элементы строк по-отдельности.

Требования к реализации: при выполнении этого задания вы можете определять любые вспомогательные функции.
Вводить или выводить что-либо не нужно. Реализовывать функцию main не нужно.
"""

def swap_min(a, m, n):
    t = 0
    mini = a[0]
    for i in range(1, m):
        if sum(a[i]) < sum(mini):
            mini = a[i]
            t = i
    a[0], a[t] = a[t], a[0]
    
    for i in range(0, m):
        for j in range(0, n):
            print(a[i][j], end = " ")
        print()
        
#пример работы в программе
        
mas = []

m = int(input("m = "))
n = int(input("n = "))

for i in range(m):
    mas.append([])
    for j in range(n):
        a = int(input())
        mas[i].append(a)

print("mas = ")

for i in range(m):
    for j in range(n):
        print(mas[i][j], end = " ")
    print()

print("swap min = ")
swap_min(mas, m, n)
