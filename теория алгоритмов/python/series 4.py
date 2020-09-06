'''
Series4. Дано целое число N и набор из N вещественных чисел.
Вывести сумму и произведение чисел из данного набора.
'''
import random
n = int(input())
mas = []
i = 0
sum = 0
pr = 1
while i < n:
    a = random.randint(1, 20)
    mas.append(a)
    i += 1
print(mas)
i = 0
while i < n:
    sum += mas[i]
    pr *= mas[i]
    i += 1
    
print(sum)
print(pr)
