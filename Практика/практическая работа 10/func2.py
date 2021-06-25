# http://ptaskbook.com/ru/tasks/func.php
# Выполнил задание Яковлев Прокопий Максимович
'''
Описать функцию IsSquare(K) логического типа, возвращающую True, 
если целый параметр K (> 0) является квадратом некоторого целого числа, и False 
в противном случае. С ее помощью найти количество квадратов в наборе из 10 целых 
положительных чисел.
'''
import math

def IsSquare(x):
    if math.sqrt(x).is_integer():
        return True
    else:
        return False

a = [int(n) for n in input('Введите 10 чисел через пробел: ').split() if IsSquare(int(n))]
print(*a)
