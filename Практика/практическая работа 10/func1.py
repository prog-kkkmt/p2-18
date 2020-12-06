# http://ptaskbook.com/ru/tasks/func.php
# Выполнил задание Михайлов Данила

'''
Описать функцию SumRange(A, B) целого типа, находящую сумму всех целых
чисел от A до B включительно (A и B — целые).
Если A > B, то функция возвращает 0.
С помощью этой функции найти суммы чисел от A до B и от B до C,
если даны числа A, B, C.
'''
def SumRange(x, y):
    s = 0
    if x < y:
        for i in range(x, y+1):
            s += i
        return s
    elif x > y:
        return 0

a, b, c = int(input()), int(input()), int(input())
print(SumRange(a, b))
print(SumRange(b, c))
