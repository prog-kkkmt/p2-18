#http://ptaskbook.com/ru/tasks/func.php
#Func6
#Выполнили: Воронцов А.А. Бурлаев З.С. Щепкин М.В. П2-18

"""
 Описать функцию SumRange(A, B) целого типа, находящую сумму всех целых 
чисел от A до B включительно (A и B — целые). Если A > B, то функция возвращает 0. 
С помощью этой функции найти суммы чисел от A до B и от B до C, если даны числа A, B, C.
"""

def SumRange(a, b):
    res = sum(range(a, b+1))
    if a > b:
        return 0
    else:
        return res
a = int(input())
b = int(input())
c = int(input())
print(SumRange(a, b))
print(SumRange(b, c))
