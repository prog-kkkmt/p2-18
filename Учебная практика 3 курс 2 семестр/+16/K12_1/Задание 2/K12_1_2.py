#Выполнил: Кузнецов Матвей
#Группа: П2-18
'''
К12_1. Техника работы с множествами

Задание 2. https://pythontutor.ru/lessons/sets/problems/number_of_coincidental/
Задача «Количество совпадающих чисел»
Условие. Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как
в первом списке, так и во втором.
'''

print(len(set(input().split())&(set(input().split()))))
