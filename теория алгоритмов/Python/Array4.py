"""
Дано целое число N (> 1), а также первый член A и знаменатель D
геометрической прогрессии. Сформировать и вывести массив размера N,
содержащий N первых членов данной прогрессии:
"""
import random
n = int(input())
mas = []
a = 1
q = 2
mas.append(a)
i = 1
while i < n:
    mas.append(a)
    a *= q
    # mas.append(a*(q**i))
    i += 1
print(mas)
