'''
Minmax4°. Дано целое число N и набор из N чисел.
Найти номер минимального элемента из данного набора.
'''
import random
n = int(input())
mas = []
i = 1
while i <= n:
    a = random.randint(1, 20)
    mas.append(a)
    i += 1
print(mas)
print(min(mas))
