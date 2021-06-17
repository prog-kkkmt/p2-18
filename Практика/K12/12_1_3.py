#Pythontutor
#https://pythontutor.ru/lessons/sets/problems/sets_intersection/
#Выполнили: Воронцов А.А. Бурлаев З.С. Щепкин М.В. П2-18

"""
Даны два списка чисел. Найдите все числа, которые входят как в первый, 
так и во второй список и выведите их в порядке возрастания.
"""

a = sorted((set(input().split()) & set(input().split())))
b = []
for i in a:
    b.append(int(i))
b = sorted(b)
for i in b:
    print(i)
