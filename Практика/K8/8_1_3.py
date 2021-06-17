#Леонид Борисович Гусятинер
#Задача 3
#Выполнили: Щепкин М.В П2-18

"""
Дано N списков целых чисел (N вводится с клавиатуры, сами списки заполняются
случайным образом). Требуется сформировать
- список, содержащий уникальные значения, попадающие в каждый из N списков
- список, содержащий уникальные значения, попадающие хотя бы в один из N списков
Решение без использования set - дополнительный бонус

"""
import random

uni_1 = [] # список, содержащий уникальные значения, попадающие в каждый из N списков
uni_2 = [] # список, содержащий уникальные значения, попадающие хотя бы в один из N списков
n = int(input())
sp = []

for k in range(n):
    vr_sp = []
    lensp = random.randint(1, 5)
    for l in range(lensp):
        vr_sp.append(random.randint(0, 10))
    sp.append(vr_sp)
print(sp)
for i in range(len(sp)):
    for j in range(0,  len(sp[i])):
        uni = sp[i][j]
        cnt = 0
        for z in range(0,  n):
            if uni in sp[z]:
                cnt += 1
                if cnt == (n) and uni not in uni_1:
                    uni_1.append(uni)
print(uni_1)
for i in range(len(sp)):
    for j in range(len(sp[i])):
       uni = sp[i][j]
       if uni not in uni_2:
           uni_2.append(uni)
print(uni_2)

