"""
Дано целое число N и набор из N чисел.
Найти номер минимального элемента из данного набора.
"""
import random
n = int(input())
mas = []
i = 1
while i <= n:
    a =  a = random.randint(-9, 9)
    mas.append(a)
    i += 1
print(mas)
print(min(mas))
