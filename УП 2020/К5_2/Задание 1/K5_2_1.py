#Выполнил: Безбородов Константин
#Группа: П2-18
'''
К5_2. Техника работы с циклическими программами _ цикл while

Задание 1. Вычислить значение sin(x) с точностью до epsilon при помощи разложения в ряд
Построить блок-схему
'''

import math

def mysin(x, eps):
    sum, an = 0.0, x
    n = 1
    while(math.fabs(an)>eps):
        sum += an
        n += 1
        an *= -x*x/(2.0*n-1.0)/(2.0*n-2.0)
    return sum

x = float(input())
epsilon = float(input())

print(f"digit = {x}, mysin = {mysin(x, epsilon)}, math.sin = {math.sin(x)}")