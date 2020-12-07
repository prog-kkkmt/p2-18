#http://ptaskbook.com/ru/tasks/func.php
#Func10
#Выполнили: Воронцов А.А. Бурлаев З.С. Щепкин М.В. П2-18

"""
Описать функцию IsSquare(K) логического типа, возвращающую True, 
если целый параметр K (> 0) является квадратом некоторого целого числа, и False 
в противном случае. С ее помощью найти количество квадратов в наборе из 10 целых 
положительных чисел.
"""

def IsSquare(K):
    for i in range(1, K):
        if i**2 == K:
            return True
            break
    return False
a = [int(input()) for x in range(10)]
for num in a:
    print(IsSquare(num))

