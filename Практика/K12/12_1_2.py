#Pythontutor
#https://pythontutor.ru/lessons/sets/problems/number_of_coincidental/
#Выполнили: Щепкин М.В. П2-18

"""
Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как 
в первом списке, так и во втором.
"""

a = input().split()
b = input().split()
c = a + b
print(len(c) - len(set(c)))
