"""
Дано целое число N и набор из N вещественных чисел.
Вывести сумму и произведение чисел из данного набора.
"""
import random
n = int(input())
mas = []
i = 0
summ = 0
pro = 1
while i < n:
    a = random.randint(-9, 9)
    mas.append(a)
    i += 1
print(mas)
i = 0
while i < n:
    summ += mas[i]
    pro *= mas[i]
    i += 1
print(summ, pro)
